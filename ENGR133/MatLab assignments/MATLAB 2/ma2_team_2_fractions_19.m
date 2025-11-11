function [F1, F2, F3] = frac(S, W, chi)
F1 = 0.5 * (1 + (S/W) - seg00(S, W, chi) );
F2 = 0.5 * ( seg00(S,W,chi) + seg01(S,W,chi) - 2 * (S/W) );
F3 = 0.5 * (1 + (S/W) - seg01(S,W,chi) );
end

function [out] = seg00(S, W, chi)
out = sqrt( 1 + (S/W)^2 + 2 * (S/W) * sin(chi) );
end

function [out] = seg01(S, W, chi)
out = sqrt( 1 + (S/W)^2 - 2 * (S/W) * sin(chi) );
end