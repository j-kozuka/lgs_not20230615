function ret = saver_readme2(prms)

jfn = 'readme.json'; % json file name
%jfn = strcat(prms.parentPath, '\', jfn);
jfn = strcat(prms.subdir{1}, jfn);

json = jsonencode(prms,'ConvertInfAndNaN',false);
fileID = fopen(jfn, 'w');
fprintf(fileID, json);
fclose(fileID);

ret = 1;

end