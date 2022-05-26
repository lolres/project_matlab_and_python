clc, clear

syms x a b

filename = fopen('integrals_matlab.txt','w'); % открываем файл на запись
fprintf(filename,'%9s%11s%11s%13s%13s%24s\n','Nomer','lim1', 'lim2', 'a', 'b', 'result');
a = randi([1, 100]); % рандомное число
b = randi([1, 100]); % рандомное число
integ = subs(int(1 / x / sqrt(a*x+b), x), a, b); % вычисляем неопределенный интеграл
tic; % начало отсчета времени выполнения алгоритма
for i = 1:100
    lim1 = randi([1, 100]); % рандомное число
    lim2 = randi([1, 100]); % рандомное число
    result = subs(integ, x, lim2) - subs(integ, x, lim1); % подставляем пределы интегрирования
    fprintf(filename,'%9d%11d%11d%13d%13d%24.6f\n', i, lim1, lim2, a, b, result); % выводим переменные
end
time_end = toc; % конец отсчета времени выполнения алгоритма
fprintf(filename, "Вычислено за " + num2str(time_end) + " секунд");
fclose(filename); % закрываем число
