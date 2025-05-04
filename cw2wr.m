load('modelSW620.mat')
load('modelSW620_rs.mat')
load('modelHS255Tnew_rs_full.mat')
load('modelHS255Tnew_rsmin_full.mat')
%%
C2 = readmatrix('HS255Trsminfullachr.csv');
C2rs = readmatrix('SW620rsachr.csv');
cw2=C2(2:height(C2),2:width(C2));
cw2rs=C2rs(2:height(C2rs),2:width(C2rs));
%%
cw2rxns=intersect(modelHS255Tnew_rsmin_full.rxns,modelSW620_rs.rxns);
cw2ids_test=findRxnIDs(modelHS255Tnew_rsmin_full,cw2rxns);
cancer_only=cw2(:,cw2ids_test);
cw2rsids_test=findRxnIDs(modelSW620_rs,cw2rxns);
cancerrs_only=cw2rs(:,cw2rsids_test);
for i=1:length(cw2ids_test)
[p1_wr(i),h1_wr(i)] = ranksum(cancerrs_only(:,i),cancer_only(:,i));
end
h_cancer_wr_single=cw2rxns(find(h1_wr==1));
[FDR,Q] = mafdr(p1_wr);
find(Q<0.05);
h_cancer_wr_multiple=cw2rxns(ans);
h_cancer_wr_high_cw2=intersect(h_cancer_wr_multiple,h_cancer_wr_single);
%%
diff=h_cancer_wr_high_cw2;
diffids=findRxnIDs(modelSW620_rs,diff);
resultCell = FEA(modelSW620_rs,diffids,'subSystems')
table(resultCell)
%writetable(ans,'ovaryfea.xls');
%%
cw2median=median(cw2)';
cw2rsmedian=median(cw2rs)';
%%
%hcc1143rxns=modelHCC1143.rxns;
cw2rsids_test=findRxnIDs(modelSW620_rs,diff);
cw2ids_test=findRxnIDs(modelSW620,diff);
cancer_only=cw2median(cw2ids_test);
cancerrs_only=cw2rsmedian(cw2rsids_test);
fc=cancerrs_only./cancer_only;
log2(fc);
table(diff,modelSW620_rs.rxnNames(cw2rsids_test),cancer_only,cancerrs_only,ans);
writetable(ans,'sw620mediafullnanalysislast50.xls');