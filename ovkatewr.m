load('modelOVKATE.mat')
load('modelOVKATE_rs.mat')
load('modelOELE_rs_full.mat')
load('modelOELE_rsmin_full.mat')
%%
C2 = readmatrix('OELErsfullachr.csv');
C2rs = readmatrix('OVKATErsachr.csv');
ovkate=C2(2:height(C2),2:width(C2));
ovkaters=C2rs(2:height(C2rs),2:width(C2rs));
%%
ovkaterxns=intersect(modelOELE_rs_full.rxns,modelOVKATE_rs.rxns);
ovkateids_test=findRxnIDs(modelOELE_rs_full,ovkaterxns);
cancer_only=ovkate(:,ovkateids_test);
ovkatersids_test=findRxnIDs(modelOVKATE_rs,ovkaterxns);
cancerrs_only=ovkaters(:,ovkatersids_test);
for i=1:length(ovkateids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=ovkaterxns(find(h1_wr==1));
[FDR,Q] = mafdr(p1_wr);
find(FDR<0.05);
h_cancer_wr_multiple=ovkaterxns(ans);
h_cancer_wr_high_ovkate=intersect(h_cancer_wr_multiple,h_cancer_wr_single);
%%
diff=h_cancer_wr_high_ovkate;
diffids=findRxnIDs(modelOVKATE_rs,diff);
resultCell = FEA(modelOVKATE_rs,diffids,'subSystems')
table(resultCell)
%%
%%
ovkatemedian=median(ovkate)';
ovkatersmedian=median(ovkaters)';
%%
%hcc1143rxns=modelHCC1143.rxns;
ovkatersids_test=findRxnIDs(modelOVKATE_rs,diff);
ovkateids_test=findRxnIDs(modelOVKATE,diff);
cancer_only=ovkatemedian(ovkateids_test);
cancerrs_only=ovkatersmedian(ovkatersids_test);
fc=cancerrs_only./cancer_only;
log2(fc);
table(diff,modelOVKATE_rs.rxnNames(ovkatersids_test),cancer_only,cancerrs_only,ans);
writetable(ans,'ovkatemediafullnanalysislast50.xls');