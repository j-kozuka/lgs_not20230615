%%% save dataset %%%%%
function ret = save_dataset(dataset, readme)

parentPath = readme.subdir{1}
dcf = 'dataset.csv'; % data csvfile name
%dcf = strcat(parentPath, '\', dcf);
dcf = strcat(parentPath, dcf);
samplePath = readme.subdir{2}
targetPath = readme.subdir{3}
% samplePath = strcat(parentPath, '\sample\');
% targetPath = strcat(parentPath, '\target\');

fid = fopen(dcf,'w');
text1 = sprintf('x:sample,t:target\n');
fprintf(fid, text1);

dNum = size(dataset.target,1);
for iLoop = 1:dNum   
    filename1 = sprintf('sd%05d.csv', iLoop);
    filename2 = sprintf('td%05d.csv', iLoop);
     
    sfn1 = strcat(samplePath, filename1);
    sfn2 = strcat(targetPath, filename2);
    
    text1 = sprintf('./sample/%s,./target/%s\n',filename1, filename2);
    fprintf(fid, text1);
    
    csvwrite(sfn1,dataset.sample(iLoop,:))
    csvwrite(sfn2,dataset.target(iLoop,:))
end
fclose(fid);

ret = 1;

end
