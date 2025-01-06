clc;
clear all;
close all;

% find file
[filepath, filename, ext] = fileparts(matlab.desktop.editor.getActiveFilename);
% name of data file
datafile = 'AirbrakeDrag.xlsx';
% path and name of the data file
inputfile = strcat(filepath,'/', datafile);
% laminar uncertainty data
LsigT = 2 * transpose(xlsread(inputfile,'Laminar','H5:H11')); %Vtotal - Model+Stand at 60Hz
Lsiga = 2 * transpose(xlsread(inputfile,'Laminar','D5:D11')); %V0offset_total - Model+Stand at 0Hz
LsigS = 2 * transpose(xlsread(inputfile,'Laminar','I5:I11')); %Vts - Stand at 60Hz
Lsigb = 2 * transpose(xlsread(inputfile,'Laminar','E5:E11')); %V0offset_ts - Stand at 0Hz
% laminar data
Lcd = transpose(xlsread(inputfile,'Laminar','O5:O11')); %O5:O11 streamline, N5:N11 bluff
Ldrag = transpose(xlsread(inputfile,'Laminar','J5:J11')); %drag
% turbulent uncertainty data
TsigT = 2 * transpose(xlsread(inputfile,'Turbulent','H5:H11')); %Vtotal - Model+Stand at 60Hz
Tsiga = 2 * transpose(xlsread(inputfile,'Turbulent','D5:D11')); %V0offset_total - Model+Stand at 0Hz
TsigS = 2 * transpose(xlsread(inputfile,'Turbulent','I5:I11')); %Vts - Stand at 60Hz
Tsigb = 2 * transpose(xlsread(inputfile,'Turbulent','E5:E11')); %V0offset_ts - Stand at 0Hz
% turbulent data
Tcd = transpose(xlsread(inputfile,'Turbulent','O5:O11')); %O5:O11 streamline, N5:N11 bluff
Tdrag = transpose(xlsread(inputfile,'Turbulent','J5:J11')); %drag
% general data
aoa = transpose(xlsread(inputfile,'Laminar','A5:A11')); %angles of attack
area = transpose(xlsread(inputfile,'Laminar','M5:M11')); %M5:M11 streamline, L5:L11 bluff

% coefficients
p = 1.18141; %rho
v = 44.66 %velocity
x = 0.0092517116 %coefficient in partial calculation for cd

% device uncertainty
dunc = (0.001/2) * ones(size(9))
% laminar uncertainty magnitudes
LTunc = sqrt(dunc.^2 + LsigT.^2)
Launc = sqrt(dunc.^2 + Lsiga.^2)
LSunc = sqrt(dunc.^2 + LsigS.^2)
Lbunc = sqrt(dunc.^2 + Lsigb.^2)
% laminar drag and cd uncertainty
LdragUnc = sqrt((10.9.*LTunc).^2+(-10.9.*Launc).^2+(-10.9.*LSunc).^2+(10.9.*Lbunc).^2)
LcdUnc = sqrt((x.*LTunc./area).^2+(-x.*Launc./area).^2+(-x.*LSunc./area).^2+(x.*Lbunc./area).^2)
% turbulent uncertainty magnitudes
TTunc = sqrt(dunc.^2 + TsigT.^2)
Taunc = sqrt(dunc.^2 + Tsiga.^2)
TSunc = sqrt(dunc.^2 + TsigS.^2)
Tbunc = sqrt(dunc.^2 + Tsigb.^2)
% turbulent drag and cd uncertainty
TdragUnc = sqrt((10.9.*TTunc).^2+(-10.9.*Taunc).^2+(-10.9.*TSunc).^2+(10.9.*Tbunc).^2)
TcdUnc = sqrt((x.*TTunc./area).^2+(-x.*Taunc./area).^2+(-x.*TSunc./area).^2+(x.*Tbunc./area).^2)

% drag plot
figure(1)
hold on
grid on
box on
title('Drag at Various Angles of Attack')
xlabel("Angles of Attack (degrees)")
ylabel('Drag (N)')
scatter(aoa, Ldrag, 'filled', 'b')
scatter(aoa, Tdrag, 'filled', 'r')
legend('Laminar', 'Turbulent')
errorbar(aoa, Ldrag, LdragUnc,'vertical', 'b', 'HandleVisibility', 'off')
errorbar(aoa, Tdrag, TdragUnc,'vertical', 'r', 'HandleVisibility', 'off')

figure(2)
hold on
grid on
box on
title('CD at Various Angles of Attack')
xlabel("Angles of Attack (degrees)")
ylabel('CD')
scatter(aoa, Lcd, 'filled', 'b')
scatter(aoa, Tcd, 'filled', 'r')
legend('Laminar', 'Turbulent')
errorbar(aoa, Lcd, LcdUnc,'vertical', 'b', 'HandleVisibility', 'off')
errorbar(aoa, Tcd, TcdUnc,'vertical', 'r', 'HandleVisibility', 'off')