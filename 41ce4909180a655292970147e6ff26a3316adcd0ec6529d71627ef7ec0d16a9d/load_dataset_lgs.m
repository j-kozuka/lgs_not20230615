close all
clear

oldpath = path;
%path(oldpath,'C:\Users\jun-ko\Dropbox\Works\jkLib\matlib') % home
path(oldpath,'D:\Users\crest\Dropbox\Works\jkLib2\matlib') % (spectra1)

db_dir = 'd:/db/'; % database
%dshash_name = '17dec9b6e50a48aa83d843647c3dec3f'; % train 
dshash_name = 'ec1e938a374d6b9706983dfe6e1fdc83'; % test
parentPath = strcat(db_dir, dshash_name, '/');

%%%%%%%%%%%%%%%%%%%%%%%%
%%% load dataset
%%%%%%%%%%%%%%%%%%%%%%%%%
dataset = reader_dataset(parentPath) % read dataset
readme = reader_readme(parentPath) % read parameters

dataset.sample
dataset.target
readme