clc;
clear;

% Assuming all the links are 10x3x3 cm in dimension
% Mass of the links are calculated based off PLA density and assumed
% dimensions for the links

l = [0.15 0.15 0.15 0.04]; % length of the links (m)
w = [0.03 0.03 0.03 0.03]; % width of the links (m)
h = [0.03 0.03 0.03 0.03]; % thickness of the links (m)
alpha = [8 8 8 8]; % angular acceleration (deg/s^2)
m = [0.03983 0.0442 0.0442 0.077]; % mass of links (kg)
M = [0.077 0.077 0.077 0.077]; % mass of motors (kg)
g = 9.81; % acceleration due to gravity (m/s^2)
Ic = (1/12)*(l.^2).*(w.^2).*m; % moment of interia through the centroid of the links
I = Ic + (l/2).^2.*m; % moment of interia about an axis through the joint
flag = 0;
maxT4 = 0;
maxT3 = 0;
maxT2 = 0;
Output=[]; 

for theta2 = 0:90
    for theta3 = 0:90
        for theta4 = 0:60
          
            T4 = I(4)*alpha(4) + m(4)*g*(l(4) /2)*cos(theta4 - theta3 + theta2);
            T3 = I(3)* alpha(3) + T4 + m(3)*g*(l(3)/2)*cos(theta3 - theta2) + m(4)*g*l(3)*cos(theta3 - theta2);
            T2 = I(2)*alpha(2) + T3 + m(2)*g*(l(2)/2)*cos(theta2) + (M(3) + m(3) + m(4))*g*l(2)*cos(theta2);
            if abs(T2) > 1.2 || abs(T3) > 1.2 || abs(T4) > 1.2
                flag = 1;
                break;
            end
            
            if T4>maxT4
                maxT4 = T4;
            end
            if T3>maxT3
                maxT3 = T3;
            end
            if T2>maxT2
                maxT2 = T2;
            end
        end
    end
end

fprintf('Maximum needed torque at joint 2: %f N-m\n', maxT2)
fprintf('Maximum needed torque at joint 3: %f N-m\n', maxT3)
fprintf('Maximum needed torque at joint 4: %f N-m\n', maxT4)

if flag == 0
    fprintf('\nThe moment at each joint is within the motor torque capacity')
else
    fprintf('\nThe motor torque is insufficient')
end

