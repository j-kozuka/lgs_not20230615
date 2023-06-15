%%%% make dataset %%%%%%
readme.dNum = 10; % number of data
readme.dimSmp = 1; % dimension of sample
readme.dimTrg = 1; % dimension of target

buf_tt = [0, 1]'; % truth table of buffer
not_tt = [1, 0]'; % truth table of not

readme.db_path = db_path;
readme.gate_tt = not_tt;

%%%%%%%%%% train dataset %%%%%%%%%%
readme_train = readme;
readme_train.dataset_code = 'lgs_not_train';
dataset_train.sample = generator_binary_sample(readme_train.dNum, readme_train.dimSmp);
dataset_train.target = gate(dataset_train.sample, not_tt); % not gate

readme_train
dataset_train

%%%%%%%%%% test dataset %%%%%%%%%%%%
readme_test = readme;
readme_test.dataset_code = 'lgs_not_test';
dataset_test.sample = generator_binary_sample(readme_test.dNum, readme_test.dimSmp);
dataset_test.target = gate(dataset_test.sample, not_tt); % not gate

readme_test
dataset_test

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%% functions %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function opt = gate(ipt, tt)
    idx = ipt+1;
    opt = tt(idx);
end

function ret = generator_binary_sample(nOd, nOs)
    %ret = randi(2, [nOs, nOd]) - 1;
    ret = randi([0,1], [nOd, nOs]);
end