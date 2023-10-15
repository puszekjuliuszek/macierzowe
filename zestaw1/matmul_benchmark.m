% Define the file path
file_path = "matrix_data.csv";

% Use the `csvread` function to read the data from the file into a matrix


% Display the read matrix
disp("Matrix read from file:");
%disp(matrix_data);

mat_names = ["matrix_data_1.csv", "matrix_data_2.csv", "matrix_data_3.csv",
"matrix_data_4.csv", "matrix_data_5.csv", "matrix_data_6.csv", "matrix_data_7.csv",
"matrix_data_8.csv", "matrix_data_9.csv", "matrix_data_10.csv", "matrix_data_11.csv",
"matrix_data_12.csv", "matrix_data_13.csv", "matrix_data_14.csv", "matrix_data_15.csv",
"matrix_data_16.csv", "matrix_data_17.csv", "matrix_data_18.csv", "matrix_data_19.csv",
"matrix_data_0.csv"];


%for i = 1:10
 %   matrix_data_1 = csvread(mat_names(2*i));
 %   matrix_data_2 = csvread(mat_names(2*i+1));
 %   tic;
 %   result = matrix_data_1 * matrix_data_2
 %   elapsed_time = toc;
 %   disp(['Elapsed time: ' num2str(elapsed_time) ' seconds']);
%endfor

matrix_data_1 = csvread("matrix_data_1.csv");
matrix_data_2 = csvread("matrix_data_2.csv");

for i  = 1:10
  tic;
  result = matrix_data_1 * matrix_data_2
  elapsed_time = toc;
  disp(['Elapsed time: ' num2str(elapsed_time) ' seconds']);
endfor
