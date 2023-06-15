function dataset = reader_dataset(datasetPath)

dcf = 'dataset.csv'; % data csvfile name
dcf = strcat(datasetPath, dcf);

dsT = readtable(dcf, 'Delimiter', ',')
dNum = size(dsT,1);
for iLoop = 1:dNum
    fpfn = strrep(char(dsT.x_sample(iLoop)),'./',datasetPath);  % full path filename
    fpfn = strrep(fpfn,'/','\');
    data = csvread(fpfn);
    dataset.sample(iLoop,:) = data;

    fpfn = strrep(char(dsT.t_target(iLoop)),'./',datasetPath);  % full path filename
    fpfn = strrep(fpfn,'/','\');
    target = csvread(fpfn);
    dataset.target(iLoop) = target;
end
dataset.target = (dataset.target)';
%dataset.target = dsT.t_target;

end