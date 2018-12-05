%data = csvread("Cleaned_Data.csv", 1, 5 );
file = 'Cleaned_Data.csv';
data = read_mixed_csv(file, ",");
lat = data(:,5);
long = data(:,6);
combined = [lat long];
len = length(combined);
for k = 1:len
    if strcmp(combined(k,1), 'nan') 
        combined(k,:) = [];
    end
    if str2double(combined(k,1)) == 0
        combined(k,:) = [];
    end 
    if k == length(combined)
        break;
    end
end
%lat then long
combined(1,:) = [];
%combined = cell2table(combined);
len = length(combined);
new_combined = [];
i = 1;
while i < 3
   j = 1;
   while j < len
        new_combined(j,i) = str2double(combined(j,i));
        j = j + 1; 
   end
   i = i + 1;
end
scatter(new_combined(:,1), new_combined(:,2));

function lineArray = read_mixed_csv(fileName, delimiter)

  fid = fopen(fileName, 'r');        
  lineArray = cell(100, 1);           
                                      
  lineIndex = 1;                     
  nextLine = fgetl(fid);              
  while ~isequal(nextLine, -1)       
        lineArray{lineIndex} = nextLine;  
        lineIndex = lineIndex+1;          
        nextLine = fgetl(fid);           
  end
  fclose(fid);                        

  lineArray = lineArray(1:lineIndex-1);              
  for iLine = 1:lineIndex-1                          
        lineData = textscan(lineArray{iLine}, '%s', ... 
                        'Delimiter', delimiter);
        lineData = lineData{1};                         
        if strcmp(lineArray{iLine}(end), delimiter)      
            lineData{end+1} = '';                        
        end
        lineArray(iLine, 1:numel(lineData)) = lineData;  
  end
end