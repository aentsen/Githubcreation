<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>랜덤 비밀번호 생성기</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: #f1f3f6;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    h1 {
      color: #333;
    }
    #password {
      font-size: 1.5rem;
      background: #fff;
      padding: 10px 20px;
      border-radius: 10px;
      box-shadow: 0 0 5px rgba(0,0,0,0.2);
      margin: 20px;
      min-width: 200px;
      text-align: center;
    }
    button {
      padding: 10px 20px;
      border: none;
      background-color: #0078ff;
      color: white;
      border-radius: 8px;
      font-size: 1rem;
      cursor: pointer;
    }
    button:hover {
      background-color: #005ecc;
    }
  </style>
</head>
<body>
  <h1>🔐 랜덤 비밀번호 생성기</h1>
  <div id="password">여기에 비밀번호가 표시됩니다</div>
  <button onclick="generatePassword()">비밀번호 생성</button>

  <script>
    function generatePassword() {
      const length = 10; // 비밀번호 길이
      const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
      let password = "";
      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
      }
      document.getElementById("password").textContent = password;
    }
  </script>
</body>
</html>
