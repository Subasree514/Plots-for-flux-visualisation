load('modelHCC1143_rs.mat');
load('modelHCC1143.mat');
load('modelHMEL_rs_full.mat')
load('modelHMEL_rsmin_full.mat')
%%
C2 = readmatrix('HMELrsminfullachr.csv');
C2rs = readmatrix('HCC1143rsachr.csv');
hcc1143=C2(2:height(C2),2:width(C2));
hcc1143rs=C2rs(2:height(C2rs),2:width(C2rs));
%%
hcc1143rxns=intersect(modelHMEL_rs_full.rxns,modelHCC1143_rs.rxns);
hcc1143ids_test=findRxnIDs(modelHMEL_rs_full,hcc1143rxns);
cancer_only=hcc1143(:,hcc1143ids_test);
hcc1143rsids_test=findRxnIDs(modelHCC1143_rs,hcc1143rxns);
cancerrs_only=hcc1143rs(:,hcc1143rsids_test);
for i=1:length(hcc1143ids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=hcc1143rxns(find(h1_wr==1));
[FDR,Q] = mafdr(p1_wr);
find(Q<0.05);
h_cancer_wr_multiple=hcc1143rxns(ans);
h_cancer_wr_high_hcc1143=intersect(h_cancer_wr_multiple,h_cancer_wr_single);
%%
diff=(h_cancer_wr_high_hcc1143);
diffids=findRxnIDs(modelHCC1143_rs,diff);
resultCell = FEA(modelHCC1143_rs,diffids,'subSystems')
table(resultCell)
%%
hcc1143median=median(hcc1143)';
hcc1143rsmedian=median(hcc1143rs)';
%%
%hcc1143rxns=modelHCC1143.rxns;
hcc1143rsids_test=findRxnIDs(modelHCC1143_rs,diff);
hcc1143ids_test=findRxnIDs(modelHCC1143,diff);
cancer_only=hcc1143median(hcc1143ids_test);
cancerrs_only=hcc1143rsmedian(hcc1143rsids_test);
fc=cancerrs_only./cancer_only;
log2(fc);
table(diff,modelHCC1143_rs.rxnNames(hcc1143rsids_test),cancer_only,cancerrs_only,ans);
writetable(ans,'hcc1143mediafullnanalysislastco250.xls');