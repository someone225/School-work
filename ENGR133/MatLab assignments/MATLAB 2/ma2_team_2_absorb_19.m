function out = dtr(in)
%degrees to radians
out = in * pi/180;
end


function [out] = absorb(F2, S, W, chi, alpha, theta)

out = (alpha * W * sin(dtr( theta + chi) ) ) / (S * cos(dtr( theta) ) * (1 - F2 * (1 - alpha)));

end