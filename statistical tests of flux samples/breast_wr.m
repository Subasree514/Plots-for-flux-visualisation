%% breast cancer models without and with RS
load('modelHCC1143_rs.mat');
load('modelHCC1143.mat');

%% breast non-cancerous models with RS
load('modelHMEL_rsmin_full.mat')

%% load rs integrated non-cancerous and cancerous flux samples
C = readmatrix('HMELrsminfullachr.csv');
Crs = readmatrix('HCC1143rsachr.csv');

%% get the numerical data (flux samples of reactions)
breast=C(2:height(C),2:width(C));
breastrs=Crs(2:height(Crs),2:width(Crs));

%% compare the fluxes of the common reactions
tnbcrxns=intersect(modelHMEL_rs_full.rxns,modelHCC1143_rs.rxns);

%% non-cancer - sample 1
tnbcids_test=findRxnIDs(modelHMEL_rs_full,tnbcrxns);
cancer_only=breast(:,tnbcids_test);

%% cancer - sample 2
tnbcrsids_test=findRxnIDs(modelHCC1143_rs,tnbcrxns);
cancerrs_only=breastrs(:,tnbcrsids_test);

%% Wilcoxon rank sum test
for i=1:length(tnbcids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=tnbcrxns(find(h1_wr==1));

%% FDR
[FDR,Q] = mafdr(p1_wr);
find(Q<0.05);
h_cancer_wr_multiple=tnbcrxns(ans);

%% Choose that satisfies both single and multiple hypothesis test results
h_cancer_wr_high_hcc1143=intersect(h_cancer_wr_multiple,h_cancer_wr_single);

%% flux enrichment analysis of the satistically different reactions
diff=(h_cancer_wr_high_hcc1143);
diffids=findRxnIDs(modelHCC1143_rs,diff);
resultCell = FEA(modelHCC1143_rs,diffids,'subSystems')
table(resultCell)
