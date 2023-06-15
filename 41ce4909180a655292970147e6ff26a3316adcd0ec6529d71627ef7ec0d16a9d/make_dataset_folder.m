%%% make_session_macro20221109
%% dataset name
function new_readme = make_dataset_folder(readme)

new_readme = readme;

readme.dataset_name = strcat(readme.dataset_code, getTimecode());
readme.dshash_name = mlreportgen.utils.hash(readme.dataset_name)
parentPath = strcat(readme.db_path, readme.dshash_name, '/');

make_directory(parentPath);

%%% make subfolder %%%%%%%%%%%%%
dir{1} = 'sample/';
dir{2} = 'target/';
dir{3} = 'model/';

new_readme.subdir{1} = parentPath;
for iLoop = 2:(length(dir)+1)
    new_readme.subdir{iLoop} = strcat(parentPath, dir{iLoop-1});
    make_directory(new_readme.subdir{iLoop});
end

% readme.dir{1} = 'sample';
% readme.dir{2} = 'target';
% readme.dir{3} = 'model';
% 
% 
% for iLoop = 1:length(readme.dir)
%     new_readme.subdir{iLoop} = strcat(parentPath, readme.dir{iLoop});
%     make_directory(new_readme.subdir{iLoop});
% end


end