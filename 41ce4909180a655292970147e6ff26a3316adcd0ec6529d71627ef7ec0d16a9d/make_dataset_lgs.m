close all
clear

oldpath = path;
%path(oldpath,'C:\Users\jun-ko\Dropbox\Works\jkLib\matlib') % home
path(oldpath,'D:\Users\crest\Dropbox\Works\jkLib2\matlib') % (spectra1)

db_path = '../'; % database path
%%%% make dataset %%%%%%
makedataset_notgate_macro

%%%% save dataset %%%%%%%%
saver_dataset(dataset_train, readme_train)
saver_dataset(dataset_test, readme_test)


%%%%%%%%%%%% function %%%%%%%%%%%%%%%%%%
function saver_dataset(dataset, readme)

readme = make_dataset_folder(readme);
save_dataset(dataset, readme)
save_readme(readme)

end

% makefolder20230615
% saver_dataset(parentPath, dataset)
% saver_readme(parentPath, readme)