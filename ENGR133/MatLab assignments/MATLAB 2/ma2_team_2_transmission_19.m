function [out] = ma2_team_2_transmission_19(F_, S, W, chi, alpha, theta)

n = (F_(2) * (1-alpha)^2 * (F_(3) + F_(1) *( F_(2) * (1-alpha) ) ) ) / ( 1 - F_(2)^2 * (1-alpha)^2 );

out = 1 - (W/S) * (sin( dtr(theta + chi) ) / cos( dtr(theta) ) ) * (1 - F_(1) * (1 - alpha) - n ) ; 

end


function out = dtr(in)
%degrees to radians
out = in * pi/180;
end



%F_test = [0.119, 0.4393, 0.4417];
%test_out = trans(F_test, 40, 50, 30, 0.5, 18);
%disp(test_out);

