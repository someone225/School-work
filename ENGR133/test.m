avector = [];
a = 1;
b = 1;
while a < 10
    if a == 5
        a = a + 2;
        continue;
    end
    avector = [avector a];
    for b = a:4:10
        if b == (a + 4);
            b = b + 4;
            break;
        end
        avector = [avector b];
    end
    a = a + 2;
end

fprintf("%d", b);