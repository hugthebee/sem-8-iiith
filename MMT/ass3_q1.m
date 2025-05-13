a = miraudio('ragtime.wav')
% mirplay(a)
mirtempo(a)

a = miraudio('vivaldi.wav')
% mirplay(a)
mirtempo(a)

a = miraudio('valse_triste_happy.wav')
% mirplay(a)
mirtempo(a)

a = miraudio('laksin.wav')
% mirplay(a)
mirtempo(a)

a = miraudio('czardas.wav')
% mirplay(a)
mirtempo(a)


a = miraudio('laksin.wav')
% mirplay(a)
mirtempo(a, 'Frame', 3, 0.5)

a = miraudio('czardas.wav')
% mirplay(a)
mirtempo(a, 'Frame', 3, 0.5)

a = miraudio('ragtime.wav')
% mirplay(a)
mirtempo(a, 'Frame', 3, 0.5)
%% pulse clarity and tempo
t = mirpulseclarity('Folder')
% t = mirtempo('Folder')
% order = mirgetdata(t)
% order = sort(order)
% 
% t = mirtempo('Rite_of_spring.mp3', 'Frame', 3,1)