%% ovarian cancer models without and with RS
load('modelOVKATE.mat')
load('modelOVKATE_rs.mat')

%% ovary non-cancerous models with RS
load('modelOELE_rsmin_full.mat')

%% load rs integrated non-cancerous and cancerous flux samples
C = readmatrix('OELErsfullachr.csv');
C_rs = readmatrix('OVKATErsachr.csv');

%% get the numerical data (flux samples of reactions)
ovary=C(2:height(C),2:width(C));
ovaryrs=C_rs(2:height(C_rs),2:width(C_rs));

%% compare the fluxes of the common reactions
ovaryrxns=intersect(modelOELE_rs_full.rxns,modelOVKATE_rs.rxns);

%% non-cancer - sample 1
ovaryids_test=findRxnIDs(modelOELE_rs_full,ovaryrxns);
cancer_only=ovary(:,ovaryids_test);

%% cancer - sample 1
ovkatersids_test=findRxnIDs(modelOVKATE_rs,ovaryrxns);
cancerrs_only=ovaryrs(:,ovkatersids_test);

%% Wilcoxon rank sum test
for i=1:length(ovaryids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=ovaryrxns(find(h1_wr==1));

%% FDR 
[FDR,Q] = mafdr(p1_wr);
find(FDR<0.05);
h_cancer_wr_multiple=ovaryrxns(ans);

%% Choose that satisfies both single and multiple hypothesis test results
h_cancer_wr_high_ovkate=intersect(h_cancer_wr_multiple,h_cancer_wr_single);

%% flux enrichment analysis of the satistically different reactions
diff=h_cancer_wr_high_ovkate;
diffids=findRxnIDs(modelOVKATE_rs,diff);
resultCell = FEA(modelOVKATE_rs,diffids,'subSystems')
table(resultCell)
