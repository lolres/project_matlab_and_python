clc, clear

syms x a b

filename = fopen('integrals_matlab.txt','w'); % открываем файл на запись
fprintf(filename,'%9s%11s%11s%13s%13s%24s\n','Nomer','lim1', 'lim2', 'a', 'b', 'result');
% печатаем шапку таблицы

a = 54; % задаем константу
b = 77; % задаем константу
lim1 = 2; % задаем предел интегрирования для отчета
lim2 = 10; % задаем предел интегрирования для отчета
integ = int(1 / x / sqrt(a*x+b), x); % вычисляем неопределенный интеграл
result = subs(integ, x, lim2) - subs(integ, x, lim1); % результат для отчета
fprintf(filename,'%9d%11d%11d%13d%13d%24.6f\n', 1, lim1, lim2, a, b, result); % выводим переменные
tic; % начало отсчета времени выполнения алгоритма
for i = 2:100
    lim1 = randi([1, 100]); % рандомное число
    lim2 = randi([1, 100]); % рандомное число
    result = subs(integ, x, lim2) - subs(integ, x, lim1); % подставляем пределы интегрирования
    fprintf(filename,'%9d%11d%11d%13d%13d%24.6f\n', i, lim1, lim2, a, b, result); % выводим переменные
end
time_end = toc; % конец отсчета времени выполнения алгоритма
fprintf(filename, "Вычислено за " + num2str(time_end) + " секунд"); % печатаем время выполнения
fclose(filename); % закрываем файл
