function [out] = ma2_team_2_absorb_19(F2, S, W, chi, alpha, theta)

out = (alpha * W * sin(theta + chi) ) / (S * cos(theta) * (1 - F2 * (1 - alpha)));

end