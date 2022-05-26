clc, clear

filetime = fopen('results_time.txt','w'); %открытие файла для результатов времени выполнения алгоритма
for i = 1:50
    filename1 = strcat('matrixs/matrix', num2str(i), '.txt');
    slau = randi([-100, 100], 100, 101); %создаем матрицу в которой содержатся 
    % матрица порядка 100 и вектор-столбец свободных членов
    writematrix(slau,filename1); % запись в файл матрицы и вектора свободных членов
    slau1 = readmatrix(filename1);
    tic; % начало отсчета времени выполнения алгоритма
    A = slau(:,1:5); % матрица А
    b = slau(:,6); % вектор свободных членов
    x=b\A; % решение СЛАУ
    time_end = toc; % конец отсчета времени выполнения алгоритма
    filename2 = strcat('results/result', num2str(i), '.txt');
    writematrix(x,filename2); % запись в файл результата вычислений 
    fprintf(filetime, "Матрица %3d: вычислено за %12.8f секунд\n", i, time_end); % запись 
    %результатов работы алгоритма
end
fclose(filetime);