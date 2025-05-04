%% colon cancer models without and with RS
load('modelSW620.mat')
load('modelSW620_rs.mat')

%% colon non-cancerous models with RS
load('modelHS255Tnew_rsmin_full.mat')

%% load rs integrated non-cancerous and cancerous flux samples
C = readmatrix('HS255Trsminfullachr.csv');
C_rs = readmatrix('SW620rsachr.csv');

%% get the numerical data (flux samples of reactions)
crc=C(2:height(C),2:width(C));
crcrs=C_rs(2:height(C_rs),2:width(C_rs));

%% compare the fluxes of the common reactions
crcrxns=intersect(modelHS255Tnew_rsmin_full.rxns,modelSW620_rs.rxns);
%% non-cancer - sample 1
crcids_test=findRxnIDs(modelHS255Tnew_rsmin_full,crcrxns);
cancer_only=crc(:,crcids_test);
%% cancer - sample 2
crcrsids_test=findRxnIDs(modelSW620_rs,crcrxns);
cancerrs_only=crcrs(:,crcrsids_test);
%% Wilcoxon rank sum test
for i=1:length(crcids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=crcrxns(find(h1_wr==1));
%% FDR
[FDR,Q] = mafdr(p1_wr);
find(Q<0.05);
h_cancer_wr_multiple=crcrxns(ans);
%% Choose that satisfies both single and multiple hypothesis test results
h_cancer_wr_high_crc=intersect(h_cancer_wr_multiple,h_cancer_wr_single);

%% flux enrichment analysis of the satistically different reactions
diff=h_cancer_wr_high_crc;
diffids=findRxnIDs(modelSW620_rs,diff);
resultCell = FEA(modelSW620_rs,diffids,'subSystems')
table(resultCell)
%writetable(ans,'ovaryfea.xls');

