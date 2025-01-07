clear all
close all
clc

dataFile = 'Moment.csv';
timeData = table2array(readtable(dataFile, Range="A2:A1705", ReadVariableNames=false));
angleData = deg2rad(table2array(readtable(dataFile, Range="B2:B1705", ReadVariableNames=false)));
torqueData = table2array(readtable(dataFile, Range="C2:C1705", ReadVariableNames=false));

figure(1);
plot(timeData, torqueData)
title('Required Torque  vs. Time')
xlabel('Time (s)') 
ylabel('Moment (Nm)') 


%% Calculate Motor 1 Voltage and Current Requirements of the Ankle
time = transpose([0.63:0.01:1.895]);
interpAngle = interp1(timeData, angleData, time);
interpTorque = interp1(timeData, torqueData, time);
smooAngle = smoothdata(interpAngle, "movmean", 5); % 50ms smoothing window (5X step)
smooTorque = smoothdata(interpTorque, "movmean", 5); % 50ms smoothing window (5X step)
omega = gradient(smooAngle, 0.01);
alpha = gradient(omega, 0.01);
torqueDot = gradient(smooTorque, 0.01);
torqueDDot = gradient(torqueDot, 0.01);

% Motor 1 constants
J = 0.12E-3; % kgm^2
kT = 0.14; % Nm/A
R = 186E-3; % Ohm   
L = 138E-6; % H
N = 45;
eff = 0.9;

inertia_current = (N * J * alpha) / kT;
load_current = (smooTorque / (N * eff)) / kT;

[v, c] = calcVal(J, kT, R, L, N, eff, omega, alpha, smooTorque, -1);
avgC = mean(abs(c))
avgV = mean(abs(v))

%% Plot Motor 1 Voltage and Current of the Ankle
figure(2)
hold on

subplot(1,2,1)
plot(time, v)
title('Motor Voltage Required')
xlabel('Time (s)') 
ylabel('Voltage (V)') 

subplot(1,2,2)
plot(time, c)
title('Motor Current Required')
xlabel('Time (s)') 
ylabel('Current (A)') 


%% Plot Influence of Motor 1 Inertia and Load Torque on Current Requirements
figure(3)
hold on

plot(time, inertia_current)
plot(time, load_current)
title('Current Demand Factors')
xlabel('Time (s)') 
ylabel('Current (Amp)')
legend('Motor Inertia', 'Load Torque')


%% Plot each Motor's Power Loss Against Transmission Ratios
N = [1:1000];
for i = N
    [v, c] = calcVal(9.25E-6, 70.5E-3, 6.28, 3.09E-3, i, 0.9, omega, alpha, smooTorque, -1);
    Ploss1(i) = mean(c(1:end-1).^2 * 6.28);
    [v, c] = calcVal(J, kT, R, L, i, eff, omega, alpha, smooTorque, -1); 
    Ploss2(i) = mean(c(1:end-1).^2 * R);
    [v, c] = calcVal(181E-7, 152E-3, 7.37, 4.27E-3, i, 0.9, omega, alpha, smooTorque, -1); 
    Ploss3(i) = mean(c(1:end-1).^2 * 7.37);
end

figure(4)
hold on

plot(N, Ploss1)
plot(N, Ploss2)
plot(N, Ploss3)
title('Motor & Transmission Ratio Combination Comparison')
xlabel('Transmission Ratio, N') 
ylabel('Power Loss (W)')
legend('Motor 1', 'Motor 2', 'Motor 3')
ylim([0 100])


%% Best Motor-Transmission Combination
[min_val, min_ind] = min(Ploss2); % minimum power loss
loss_45 = Ploss2(45) % optimal power loss to fit within voltage range (N = 45)


%% Exam 1
figure(5)
hold on
[v, cSEA] = calcVal(J, kT, R, L, 45, eff, omega, alpha, smooTorque, 50); 
[v, c] = calcVal(J, kT, R, L, 45, eff, omega, alpha, smooTorque, -1);
plot(time, cSEA)
plot(time, c)
legend('Series Elastic Actuator', 'No SEA')
title('Current Requirements vs. Time')
xlabel('Time (s)') 
ylabel('Current (Amp)')

SEA = [10:10:1000];
ind = 1;

for i = SEA
    [v, cSEA] = calcVal(J, kT, R, L, 75, eff, omega, alpha, smooTorque, i);
    Ploss75(ind) = mean(cSEA(1:end-1).^2 * R);
    [v, cSEA] = calcVal(J, kT, R, L, 90, eff, omega, alpha, smooTorque, i);
    Ploss90(ind) = mean(cSEA(1:end-1).^2 * R);
    [v, cSEA] = calcVal(J, kT, R, L, 45, eff, omega, alpha, smooTorque, i);
    Ploss45(ind) = mean(cSEA(1:end-1).^2 * R);

    ind = ind + 1;
end

% Minimized Power Loss. Multiply by 10 for true N
[val75, ind75] = min(Ploss75);
[val90, ind90] = min(Ploss90);
[val45, ind45] = min(Ploss45);

figure(6)
hold on
plot(SEA, Ploss75)
plot(SEA, Ploss90)
plot(SEA, Ploss45)
title('Power Loss at Various SEA Stiffnesses')
xlabel('Stiffnesses (Nm/rad)') 
xlim([00 800])
ylim([2.5 8])
ylabel('Power Loss (W)')
legend('N = 75', 'N = 90', 'N = 45')

% Plot current and voltage vs. time for optimal SEAs
figure(7)
hold on
[v75, c75] = calcVal(J, kT, R, L, 75, eff, omega, alpha, smooTorque, ind75 * 10);
[v90, c90] = calcVal(J, kT, R, L, 90, eff, omega, alpha, smooTorque, ind90 * 10);
[v45, c45] = calcVal(J, kT, R, L, 45, eff, omega, alpha, smooTorque, ind45 * 10);

subplot(2,1,1)
hold on
plot(time, c75)
plot(time, c90)
plot(time, c45)
legend('N = 75', 'N = 90', 'N = 45')
title('Current vs. Time')
xlabel('Time (s)') 
ylabel('Current (Amp)')

subplot(2,1,2)
hold on
plot(time, v75)
plot(time, v90)
plot(time, v45)
legend('N = 75', 'N = 90', 'N = 45')
title('Voltage vs. Time')
xlabel('Time (s)') 
ylabel('Voltage (V)')

% Plot Power Loss vs Electrical Input
figure(8)
hold on
[vBest, cBest] = calcVal(J, kT, R, L, 45, eff, omega, alpha, smooTorque, -1);
%PlossBest = cSEA(1:end).^2 * R;
PlossBest = cBest(1:end).^2 * R;
e_in = vBest + (cBest * R) + (L * gradient(cBest, 0.01)); % vBest is em
P_in = e_in .* cBest;
plot(time, PlossBest)
plot(time, P_in)
legend('Power Loss','Electrical Power Input')
title('Power Input and Loss vs. Time')
xlabel('Time (s)') 
ylabel('Power (W)')

avgP = mean(abs(P_in))

%% Computation Engine
function [voltage, current] = calcVal(J, kT, R, L, N, eff, omega, alpha, smooTorque, kSEA)
    current = ((N * J * alpha) + (smooTorque / (N * eff))) / kT; % current = inertia_current + load_current

    if ~(kSEA == -1)
        torqueDot = gradient(smooTorque, 0.01);
        torqueDDot = gradient(torqueDot, 0.01);
        current = ((N .* J .* (alpha + torqueDDot ./ kSEA)) + (smooTorque / (N * eff))) / kT; % with SEA
    end
       
    voltage = (current * R) + (L * gradient(current)) + (N * kT * omega);
end

