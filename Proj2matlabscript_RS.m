%data = csvread("Cleaned_Data.csv", 1, 5 );
file1 = 'Cleaned_2017.csv';
file2 = 'Cleaned_2018.csv';
full_data1 = read_mixed_csv(file1, ",");
full_data2 = read_mixed_csv(file2, ",");
lat1 = full_data1(:,5);
long1 = full_data1(:,6);
lat2 = full_data2(:,5);
long2 = full_data2(:,6);
street2017 = full_data1(:, 9);
street2018 = full_data2(:, 9);
street2017(1) = [];
street2018(1) = [];

combined1 = [lat1 long1];
combined2 = [lat2 long2];

len1 = length(combined1);

for k = 1:len1
    if k >= length(combined1)
        break;
    end
    if strcmp(combined1(k,1), 'nan') %REMOVE NAN LONG/LAT
        combined1(k,:) = [];
    end
    if str2double(combined1(k,1)) == 0 % REMOVE ANY 0,0
        combined1(k,:) = [];
    end
    if str2double(combined1(k,1)) < 40.78 % REMOVE 6 OUTLIERS 
        combined1(k,:) = [];
    end
    
end
len2 = length(combined2);
for j = 1:len2
    if j >= length(combined2)
        break;
    end
    if strcmp(combined2(j,1), 'nan') %REMOVE NAN LONG/LAT
        combined2(j,:) = [];
    end
    if str2double(combined2(j,1)) == 0 % REMOVE ANY 0,0
        combined2(j,:) = [];
    end
    if str2double(combined2(j,2)) < 40.78 % REMOVE 6 OUTLIERS 
        combined2(j,:) = [];
    end
    if str2double(combined2(j,2)) > -73 % REMOVE 6 OUTLIERS 
        combined2(j,:) = [];
    end
    
end
%lat then long
combined1(1,:) = [];
combined2(1,:) = [];
%combined = cell2table(combined);
len1 = length(combined1);
len2 = length(combined2);
new_combined1 = [];
i = 1;
while i < 3
   j = 1;
   while j < len1
        new_combined1(j,i) = str2double(combined1(j,i));
        j = j + 1; 
   end
   i = i + 1;
end
new_combined2 = [];
i = 1;
while i < 3
   j = 1;
   while j < len2
        new_combined2(j,i) = str2double(combined2(j,i));
        j = j + 1; 
   end
   i = i + 1;
end
figure(1);
scatter(new_combined1(:,1), new_combined1(:,2));
title('Bronx Crashes 2017');
xlabel('Latitude');
ylabel('Longitude');
figure(2);
scatter(new_combined2(:,1), new_combined2(:,2));
title('Bronx Crashes 2018');
xlabel('Latitude');
ylabel('Longitude');
data2017 = array2table(new_combined1);
data2017.Properties.VariableNames = {'Latitude' 'Longitude'};
data2018 = array2table(new_combined2);
data2018.Properties.VariableNames = {'Latitude' 'Longitude'};
len1 = length(new_combined1);
len2 = length(new_combined2);
id1 = [];
for n = 1:len1
    id1(n,1) = n;
end
id2 = [];
for n = 1:len2
    id2(n,1) = n;
end
ID1 = array2table(id1);
ID2 = array2table(id2);
data2017 = [ID1 data2017];
data2018 = [ID2 data2018];
data2017.Properties.VariableNames = {'ID' 'Latitude' 'Longitude'};
data2018.Properties.VariableNames = {'ID' 'Latitude' 'Longitude'};
%CLUSTERING
% p_data  = data(:,2:3);
% p_data = table2array(p_data);
% %find the kmeans cluster centriods and plot those centers
% [idx, C] = kmeans(p_data, 100);
% %C; %remove semi to print
% figure(2);
% scatter( p_data(:,1), p_data(:,2));
% hold on;
% plot(C(:,1),C(:,2),'kx','MarkerSize',10,'LineWidth',3);
% title('Bronx Crashes Kmeans Centers');
% xlabel('Latitude');
% ylabel('Longitude');
% figure(3);
% heatmap(data, 'Latitude', 'Longitude');

%%%%%%%%%%%%%%%%%%%%%%%%%%%% on street accidents
[I, ~] = find(cellfun(@(s) isequal(s, 'nan'), street2017));
street2017(I, :) = [];

[I, ~] = find(cellfun(@(s) isequal(s, 'nan'), street2018));
street2018(I, :) = [];

len1 = length(street2017);
for k = 1:len1
   street2017(k,1) = strtrim(street2017(k,1));
end
len2 = length(street2018);
for k = 1:len2
   street2018(k,1) = strtrim(street2018(k,1));
end

street2017 = cell2table(street2017);
street2018 = cell2table(street2018);

len1 = height(street2017);
street_count2017 = table();
street1 ={};
count1 = {};
for k = 1:len1
    street = street2017{k,1};
    len = length(street1);
    if len == 0
        street1{1,1} = street;
        count1{1,1} = 1;
    else
        for j = 1:len
           if strcmp(street1{j,1}, street)
               count1{j,1} = count1{j, 1} + 1;
               break
           elseif j == len 
               street1{j+1,1} = street;
               count1{j+1,1} = 1;
               break
           end
        end
    end
end
sCount1 = [street1 count1];
street_count2017 = cell2table(sCount1);

len2 = height(street2018);
street_count2018 = table();
street2 ={};
count2 = {};
for k = 1:len2
    street = street2018{k,1};
    len = length(street2);
    if len == 0
        street2{1,1} = street;
        count2{1,1} = 1;
    else
        for j = 1:len
           if strcmp(street2{j,1}, street)
               count2{j,1} = count2{j, 1} + 1;
               break
           elseif j == len 
               street2{j+1,1} = street;
               count2{j+1,1} = 1;
               break
           end
        end
    end
end
sCount2 = [street2 count2];
street_count2018 = cell2table(sCount2);
street_count2017 = sortrows(street_count2017,-2);
c1 = categorical(street_count2017{1:10,1});
figure(3);
bar(c1, street_count2017{1:10,2});
title('Top 10 Dangerous Streets in Bronx by Amount of Acciddents (2017)');
xlabel('Street');
ylabel('Number of  Accidents')

street_count2018 = sortrows(street_count2018,-2);
c2 = categorical(street_count2018{1:10,1});
figure(4);
bar(c2, street_count2018{1:10,2});
title('Top 10 Dangerous Streets in Bronx by Amount of Acciddents (2018)');
xlabel('Street');
ylabel('Number of  Accidents')

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