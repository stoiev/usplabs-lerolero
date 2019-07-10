<html>
    <style>
        h1 {
            text-align: center;
        }
        p {
            text-indent: 70px;
            line-height: 1.5;
        }
    </style>
<body>
    <h1>{{title}}</h1>
    % for paragraph in text:
        <p>{{paragraph}}</p>
    % end
</body>
</html>