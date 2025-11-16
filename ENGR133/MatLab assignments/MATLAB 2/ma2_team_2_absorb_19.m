function [out] = ma2_team_2_absorb_19(F2, S, W, chi, alpha, theta)

out = (alpha * W * sin(dtr( theta + chi) ) ) / (S * cos(dtr( theta) ) * (1 - F2 * (1 - alpha)));

end

function out = dtr(in)
%degrees to radians
out = in * pi/180;
end




%test = absorb(0.4393 ,40, 50, 30, 0.5, 18);
%disp(test);