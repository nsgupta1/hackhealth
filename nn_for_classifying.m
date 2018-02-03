input_matrix =transpose(InputData);
% input_matrix
target_matrix = transpose(Target);
% target_matrix

full_classify = newff(minmax(input_matrix),[400 370 370 1],{'logsig','tansig','tansig','purelin'}); 
%%%---Train Network---%%%
[full_classify,tr] = trainscg(full_classify,input_matrix,target_matrix);