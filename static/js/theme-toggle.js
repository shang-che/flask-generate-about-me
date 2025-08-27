// 等待整個 HTML 文件被完整載入和解析後再執行
document.addEventListener('DOMContentLoaded', function() {
    
    // 獲取需要操作的元素
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const docElement = document.documentElement;

    // 檢查 localStorage 中是否有儲存的主題偏好
    const currentTheme = localStorage.getItem('theme');

    // 初始化主題：優先使用 localStorage 的設定，其次是系統偏好
    if (currentTheme) {
        docElement.setAttribute('data-theme', currentTheme);
        // 如果是深色模式，更新圖示為太陽
        if (currentTheme === 'dark') {
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        }
    } else {
        // 如果沒有儲存的偏好，檢查使用者的系統偏好
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefersDark) {
            docElement.setAttribute('data-theme', 'dark');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        }
    }

    // 監聽按鈕的點擊事件
    themeToggle.addEventListener('click', () => {
        // 取得目前的主題屬性
        const currentTheme = docElement.getAttribute('data-theme');

        if (currentTheme === 'dark') {
            // 切換到淺色模式
            docElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon');
        } else {
            // 切換到深色模式
            docElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun');
        }
    });

});