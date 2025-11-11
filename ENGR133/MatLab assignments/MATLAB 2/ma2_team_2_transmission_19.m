function [out] = trans(F_, S, W, chi, theta, alpha)

n = (F_(2) * (1-alpha)^2 * (F_(3) + F_(1) * F_(2) * (1-alpha) ) ) / ( 1 - F_(2)^2 * (1-alpha)^2 )

out = 1 - (W/S) * (sin(theta + chi) / cos(theta) * (1 - F_(1) * (1 - alpha) - n  ) ); 

end