

function [out] = seg00(S, W, chi)
out = sqrt( 1 + (S/W)^2 + 2 * (S/W) * sin(dtr(chi)) );
end

function [out] = seg01(S, W, chi)
out = sqrt( 1 + (S/W)^2 - 2 * (S/W) * sin(dtr(chi)) );
end

function out = dtr(in)
%degrees to radians
out = in * pi/180;
end

function [F_] = frac(S, W, chi)
F1 = 0.5 * (1 + (S/W) - seg00(S, W, chi) );
F2 = 0.5 * ( seg00(S,W,chi) + seg01(S,W,chi) - 2 * (S/W) );
F3 = 0.5 * (1 + (S/W) - seg01(S,W,chi) );

F_ = zeros(1, 3);

F_(1) = F1;
F_(2) = F2;
F_(3) = F3;

end

