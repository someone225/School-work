%% surfaceArea = 25ft / swimmer
%% minDepth = 10ft when divingBoards = 1
%% circulationCount = 3/day
    %%1 day = 24hrs = 1440 minutes
    %%therefore minCirculationRate = 3 * volume/1440 per min
%% circulationPumpRate = 15gal / min
    %%therefore pumps = minCirculationRate / 15


function [volume, dims, maxSwimmers, minPumpRate, pumps] = matchData (swimmers, divingIndicator, dataFileName)
%matchData - returns data of closest match to inputs
% args:
%   swimmers <int> <- target amount of swimmers in the desired pool
%   divingIndicator <bool 0,1> <- whether or not the desired pool has a
%                                 diving board
%   dataFileName <str> <- file name of input csv file to match for
%
% outputs:
%   volume <float> -> matched pool volume
%   dims <1d arr> -> dimensions (depth, length, width) of matched pool data
%   maxSwimmers <int> -> max amount of swimmers allowable in matched pool
%                        data
%   minPumpRate <float> -> minimum pump rate required to support matched
%                          pool data
%   pumps <int> -> minimum number of pumps required to support matched pool
%                  data

    t = importdata(dataFileName);
    data = t.data;

    L0 = size(data);
    L = L0(1);
    W = L0(2);


    tarArea = swimmers * 25;
    if(divingIndicator == 1)
        minDepth = 10;
    
    elseif(divingIndicator == 0)
        minDepth = 0;
    end
    poolVolume = zeros(1, L);
    poolDims = zeros(L, W - 1);
    

    %split data into volume and dimensions matrices
    cv = 1;
    for i = 1:L   
        for j = 1:W
            if(j == 1)
                poolVolume(cv) = data(i,j);
                cv = cv + 1;
            else
                poolDims(i, j - 1) = data(i, j);
                
            end
        end
    end


    %calculate number of valid data sets using minDepth as referance
    validIndexCount = 0;
    for i = 1:L
        if(poolDims(i, 1) >= minDepth)
            validIndexCount = validIndexCount + 1;
        end
    end
 
    validIndexes = zeros(1, validIndexCount);

    ci = 1;
    for i = 1:L
        if(poolDims(i, 1) >= minDepth)
            validIndexes(ci) = i;
            ci = ci + 1;
        end
    end

    %disp(validIndexes);

    

    %calculate error margins for each data set
    diff = zeros(1,validIndexCount);
    for i = 1:length(validIndexes)
        diff(i) = ( poolDims(validIndexes(i), 2) * poolDims(validIndexes(i), 3) ) - tarArea; 
    end

    %disp(diff);
    
    minDiff = getMin(diff);

    %find data set with least margin of error
    tarDiffIndex = 1;
    for i = 1:length(diff)
        if(diff(i) == minDiff)
            tarDiffIndex = i;
            break;
        end
    end
    %disp(tarDiffIndex);

    
    
    matchedArea = diff(tarDiffIndex) + tarArea;
    %disp(matchedArea);

    maxSwimmers = matchedArea / 25;
    %disp(maxSwimmers);

   

   %match with data of least error
   tarIndex = 1;
   for i = 1:length(poolDims)
       if(poolDims(i, 2) * poolDims(i, 3) == matchedArea)
           tarIndex = i;
           break;
       end
   end

   %disp(tarIndex);


   dSize = size(poolDims);
   dims = zeros(1, dSize(2));
   for i = 1:dSize(2)
        dims(i) = poolDims(tarIndex, i);
   end
   %disp(dims)
   

   volume = poolVolume(tarIndex);
   %disp(volume);
   minPumpRate = 3 * volume / 1440;
   %disp(minPumpRate);
   pumps = ceil(minPumpRate / 15);
   %disp(pumps);
end

function min = getMin(arr)
min = arr(1);

    for i = 1:length(arr)
        if(arr(i) < min && arr(i) >= 0)
            min = arr(i);
        end
    end

end


%%test code
[v, d, s, pRate, pNum] = matchData(10, 1, "Data_pool_info.csv");

disp(pNum);

    