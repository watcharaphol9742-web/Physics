<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A-Level Physics Master - แอปฝึกทำโจทย์ฟิสิกส์เตรียมสอบ</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Font: Prompt -->
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body {
            font-family: 'Prompt', sans-serif;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-in {
            animation: fadeIn 0.3s ease-out forwards;
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 min-h-screen text-slate-100 flex flex-col justify-between selection:bg-indigo-500 selection:text-white">

    <!-- Header Navigation -->
    <header class="w-full border-b border-indigo-900/50 bg-slate-950/60 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3 cursor-pointer" onclick="app.returnToHome()">
                <div class="bg-indigo-600 text-white p-2 rounded-xl shadow-lg shadow-indigo-500/30 flex items-center justify-center">
                    <i data-lucide="atom" class="w-6 h-6 animate-spin" style="animation-duration: 10s;"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg text-white leading-tight">A-Level Physics Master</h1>
                    <p class="text-xs text-indigo-400 font-medium">ระบบฝึกทำโจทย์ฟิสิกส์สนามสอบ TCAS</p>
                </div>
            </div>
            <div id="user-stats" class="hidden sm:flex items-center space-x-4 bg-indigo-950/80 border border-indigo-800/50 px-3 py-1.5 rounded-full text-xs font-medium text-indigo-200">
                <span id="nav-category-badge" class="bg-indigo-600/60 px-2 py-0.5 rounded-full">ทั่วไป</span>
                <span id="nav-score-badge">คะแนนสะสม: 0</span>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-3xl w-full mx-auto px-4 py-8 flex-grow flex flex-col justify-center">

        <!-- Screen 1: Category Selection -->
        <div id="screen-home" class="space-y-6 animate-fade-in">
            <div class="text-center space-y-3 py-4">
                <span class="inline-block bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">
                    เตรียมตัวสอบ A-Level ฟิสิกส์
                </span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
                    เลือกหมวดหมู่โจทย์ที่คุณต้องการฝึกฝน
                </h2>
                <p class="text-slate-400 text-sm sm:text-base max-w-xl mx-auto">
                    คลังข้อสอบฟิสิกส์เน้นหน่วย SI ชัดเจน พร้อมเฉลยภาษาไทยอ่านง่ายและกระดานทดเลขในตัว
                </p>
            </div>

            <!-- Question Count Selector -->
            <div class="bg-slate-900/90 border border-indigo-900/50 p-4 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 shadow-lg">
                <div class="flex items-center space-x-2 text-xs font-medium text-slate-300">
                    <i data-lucide="sliders" class="w-4 h-4 text-indigo-400"></i>
                    <span>กำหนดจำนวนข้อที่ต้องการทำต่อชุด:</span>
                </div>
                <div class="flex items-center space-x-1.5 flex-wrap justify-end">
                    <button onclick="app.setQuestionCount(5)" id="count-btn-5" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-indigo-600 text-white shadow-md shadow-indigo-600/30">5 ข้อ</button>
                    <button onclick="app.setQuestionCount(10)" id="count-btn-10" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">10 ข้อ</button>
                    <button onclick="app.setQuestionCount(20)" id="count-btn-20" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">20 ข้อ</button>
                    <button onclick="app.setQuestionCount(30)" id="count-btn-30" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">30 ข้อ</button>
                    <button onclick="app.setQuestionCount('all')" id="count-btn-all" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">ทั้งหมด</button>
                </div>
            </div>

            <!-- Timer Duration Selector -->
            <div class="bg-slate-900/90 border border-indigo-900/50 p-4 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 shadow-lg">
                <div class="flex items-center space-x-2 text-xs font-medium text-slate-300">
                    <i data-lucide="clock" class="w-4 h-4 text-amber-400"></i>
                    <span>กำหนดเวลารวมในการทำข้อสอบ:</span>
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="app.setTimerDuration(15)" id="timer-btn-15" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-indigo-600 text-white shadow-md shadow-indigo-600/30">15 นาที</button>
                    <button onclick="app.setTimerDuration(30)" id="timer-btn-30" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">30 นาที</button>
                    <button onclick="app.setTimerDuration(45)" id="timer-btn-45" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">45 นาที</button>
                    <button onclick="app.setTimerDuration(60)" id="timer-btn-60" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700">60 นาที</button>
                </div>
            </div>

            <!-- Categories Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 pt-2">
                <!-- Card 1: Mechanics -->
                <div onclick="app.startQuiz('mechanics')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-blue-500/10 text-blue-400 rounded-xl group-hover:bg-blue-500 group-hover:text-white transition-colors">
                            <i data-lucide="gauge" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">บทหลัก</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">กลศาสตร์</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">การเคลื่อนที่ m/s, ความเร่ง m/s², มวล kg, แรง N และพลังงาน J</p>
                </div>

                <!-- Card 2: Electricity -->
                <div onclick="app.startQuiz('electricity')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-amber-500/10 text-amber-400 rounded-xl group-hover:bg-amber-500 group-hover:text-white transition-colors">
                            <i data-lucide="zap" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">บทหลัก</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">ไฟฟ้าและแม่เหล็ก</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">ประจุ C, กระแส A, ความต่างศักย์ V, ความต้านทาน ohm และกำลัง W</p>
                </div>

                <!-- Card 3: Waves -->
                <div onclick="app.startQuiz('waves')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-emerald-500/10 text-emerald-400 rounded-xl group-hover:bg-emerald-500 group-hover:text-white transition-colors">
                            <i data-lucide="waves" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">บทหลัก</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">คลื่นและแสง</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">ความถี่ Hz, ความยาวคลื่น m, อัตราเร็ว m/s และระยะทาง m</p>
                </div>

                <!-- Card 4: Modern Physics -->
                <div onclick="app.startQuiz('modern')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-purple-500/10 text-purple-400 rounded-xl group-hover:bg-purple-500 group-hover:text-white transition-colors">
                            <i data-lucide="sparkles" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">บทหลัก</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">ฟิสิกส์ยุคใหม่</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">พลังงาน eV, โฟตอน, ความยาวคลื่น de Broglie และกัมมันตรังสี</p>
                </div>

                <!-- Card 5: Fluids -->
                <div onclick="app.startQuiz('fluids')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-cyan-500/10 text-cyan-400 rounded-xl group-hover:bg-cyan-500 group-hover:text-white transition-colors">
                            <i data-lucide="droplet" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">มาใหม่</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">ของไหลและความตึงผิว</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">ความดัน Pa, ความหนาแน่น kg/m³, อัตราเร็ว m/s และแรงตึงผิว N/m</p>
                </div>

                <!-- Card 6: Thermal Physics -->
                <div onclick="app.startQuiz('thermo')" class="group relative bg-slate-900/80 border border-indigo-900/50 hover:border-indigo-500 p-6 rounded-2xl cursor-pointer transition-all duration-300 hover:shadow-xl hover:shadow-indigo-500/10 hover:-translate-y-1">
                    <div class="flex items-center justify-between mb-4">
                        <div class="p-3 bg-rose-500/10 text-rose-400 rounded-xl group-hover:bg-rose-500 group-hover:text-white transition-colors">
                            <i data-lucide="flame" class="w-6 h-6"></i>
                        </div>
                        <span class="text-xs text-slate-500 group-hover:text-indigo-300 transition-colors">มาใหม่</span>
                    </div>
                    <h3 class="text-lg font-bold text-white mb-1 group-hover:text-indigo-300 transition-colors">ความร้อนและแก๊ส</h3>
                    <p class="text-slate-400 text-xs leading-relaxed">อุณหภูมิ K หรือ °C, ปริมาตร m³, พลังงาน J และความร้อน J/kg</p>
                </div>
            </div>

            <!-- Challenge Mode Card -->
            <div onclick="app.startQuiz('challenge')" class="group relative bg-gradient-to-r from-amber-950/40 via-indigo-950/80 to-purple-950/40 border-2 border-amber-500/50 hover:border-amber-400 p-6 rounded-2xl cursor-pointer transition-all duration-300 shadow-xl shadow-amber-500/10 hover:-translate-y-1">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-4">
                        <div class="p-4 bg-amber-500 text-slate-950 rounded-2xl shadow-lg shadow-amber-500/30 group-hover:scale-110 transition-transform">
                            <i data-lucide="zap" class="w-7 h-7 fill-current"></i>
                        </div>
                        <div>
                            <span class="text-xs bg-amber-500/20 text-amber-300 px-2.5 py-0.5 rounded-full font-semibold uppercase tracking-wider">โหมดพิเศษสำหรับคนเก่ง</span>
                            <h3 class="text-xl font-extrabold text-white mt-1 group-hover:text-amber-300 transition-colors">โหมดชาเลนจ์พิเศษ (โจทย์ยากเน้นคิดวิเคราะห์)</h3>
                            <p class="text-slate-300 text-xs sm:text-sm mt-1">รวมโจทย์ประยุกต์ขั้นสูง วัดการคิดวิเคราะห์หลายขั้นตอน หน่วย SI ครบถ้วนทุกตัวแปร</p>
                        </div>
                    </div>
                    <div class="hidden sm:flex items-center justify-center p-3 bg-amber-500/10 text-amber-400 rounded-xl group-hover:bg-amber-500 group-hover:text-slate-950 transition-colors">
                        <i data-lucide="arrow-right" class="w-6 h-6"></i>
                    </div>
                </div>
            </div>

            <!-- Quick Start All Button -->
            <div class="pt-2 flex justify-center">
                <button onclick="app.startQuiz('all')" class="w-full sm:w-auto bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white font-semibold px-8 py-3.5 rounded-xl shadow-lg shadow-indigo-600/30 transition-all flex items-center justify-center space-x-2">
                    <i data-lucide="play" class="w-5 h-5 fill-current"></i>
                    <span>ทำโจทย์รวมทุกหมวดหมู่ (แบบสุ่ม)</span>
                </button>
            </div>
        </div>

        <!-- Screen 2: Quiz Interface -->
        <div id="screen-quiz" class="hidden space-y-6 animate-fade-in">
            <!-- Quiz Top Bar: Progress & Timer -->
            <div class="bg-slate-900/90 border border-indigo-900/50 p-4 rounded-2xl flex flex-col sm:flex-row justify-between items-center gap-4">
                <div class="w-full sm:w-1/2 space-y-1">
                    <div class="flex justify-between text-xs text-slate-400 font-medium">
                        <span id="quiz-progress-text">คำถามที่ 1 จาก 5</span>
                        <span id="quiz-category-label" class="text-indigo-400">กลศาสตร์</span>
                    </div>
                    <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                        <div id="quiz-progress-bar" class="bg-gradient-to-r from-indigo-500 to-violet-500 h-full w-0 transition-all duration-300"></div>
                    </div>
                </div>
                <div class="flex items-center space-x-3 flex-wrap justify-end">
                    <div class="flex items-center space-x-2 bg-slate-950 px-3 py-1.5 rounded-xl border border-slate-800 text-xs font-mono text-amber-400">
                        <i data-lucide="clock" class="w-4 h-4"></i>
                        <span id="quiz-timer">15:00</span>
                    </div>
                    <button onclick="app.toggleTimer()" id="timer-pause-btn" class="text-xs text-amber-400 hover:text-white bg-amber-500/10 hover:bg-amber-500/20 px-2 py-1.5 rounded-xl transition-colors flex items-center justify-center" title="หยุด/เริ่มเวลาชั่วคราว">
                        <i data-lucide="pause" class="w-3.5 h-3.5" id="timer-icon"></i>
                    </button>
                    <button onclick="app.resetTimer()" class="text-xs text-slate-400 hover:text-white bg-slate-800/50 hover:bg-slate-800 px-2 py-1.5 rounded-xl transition-colors flex items-center justify-center" title="รีเซ็ตเวลา">
                        <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="app.openScratchpad()" class="bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/40 px-3 py-1.5 rounded-xl text-xs font-medium flex items-center space-x-1.5 transition-all shadow-sm">
                        <i data-lucide="edit-3" class="w-4 h-4"></i>
                        <span>กระดาษทด</span>
                    </button>
                    <button onclick="app.returnToHome()" class="text-xs text-slate-400 hover:text-white bg-slate-800/50 hover:bg-slate-800 px-3 py-1.5 rounded-xl transition-colors">
                        ออก
                    </button>
                </div>
            </div>

            <!-- Question Card -->
            <div class="bg-slate-900/90 border border-indigo-900/50 p-6 sm:p-8 rounded-2xl shadow-xl space-y-6">
                <!-- Question Header -->
                <div class="flex items-start justify-between gap-4">
                    <h3 id="question-text" class="text-base sm:text-lg font-semibold text-white leading-relaxed">
                        โจทย์คำถามจะแสดงที่นี่...
                    </h3>
                </div>

                <!-- Options List -->
                <div id="options-container" class="space-y-3">
                    <!-- Options generated dynamically -->
                </div>

                <!-- Explanation Box (Hidden initially) -->
                <div id="explanation-box" class="hidden mt-6 p-5 rounded-xl border bg-slate-950/80 space-y-3 animate-fade-in">
                    <div class="flex items-center space-x-2 font-semibold text-sm" id="explanation-title">
                        <!-- Correct/Incorrect badge -->
                    </div>
                    <p id="explanation-text" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></p>
                </div>

                <!-- Next Button Container -->
                <div id="action-container" class="pt-4 flex justify-end hidden">
                    <button onclick="app.nextQuestion()" class="bg-indigo-600 hover:bg-indigo-500 text-white font-medium px-6 py-2.5 rounded-xl transition-all shadow-lg shadow-indigo-600/30 flex items-center space-x-2 text-sm">
                        <span id="next-btn-text">ข้อถัดไป</span>
                        <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Screen 3: Result Summary -->
        <div id="screen-result" class="hidden space-y-6 animate-fade-in text-center">
            <div class="bg-slate-900/90 border border-indigo-900/50 p-8 rounded-3xl shadow-xl space-y-6 max-w-lg mx-auto">
                <div class="w-20 h-20 bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 rounded-full flex items-center justify-center mx-auto shadow-inner">
                    <i data-lucide="trophy" class="w-10 h-10"></i>
                </div>
                
                <div class="space-y-2">
                    <h2 class="text-2xl sm:text-3xl font-extrabold text-white">สรุปผลการฝึกฝน</h2>
                    <p id="result-message" class="text-indigo-400 font-medium text-sm">ยอดเยี่ยมมาก! คุณทำคะแนนได้ดีเยี่ยม</p>
                </div>

                <div class="grid grid-cols-2 gap-4 py-4 border-y border-slate-800">
                    <div class="space-y-1">
                        <span class="text-xs text-slate-400">คะแนนที่คุณทำได้</span>
                        <div class="text-3xl font-bold text-white" id="final-score">4/5</div>
                    </div>
                    <div class="space-y-1">
                        <span class="text-xs text-slate-400">เวลาที่ใช้ทั้งหมด</span>
                        <div class="text-3xl font-bold text-white font-mono" id="final-time">01:25</div>
                    </div>
                </div>

                <div class="flex flex-col sm:flex-row gap-3 pt-2">
                    <button onclick="app.restartQuiz()" class="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white font-medium py-3 rounded-xl transition-all shadow-lg shadow-indigo-600/30 text-sm flex items-center justify-center space-x-2">
                        <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                        <span>ทำแบบทดสอบอีกครั้ง</span>
                    </button>
                    <button onclick="app.returnToHome()" class="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-300 font-medium py-3 rounded-xl transition-all text-sm flex items-center justify-center space-x-2">
                        <i data-lucide="home" class="w-4 h-4"></i>
                        <span>เลือกหมวดหมู่ใหม่</span>
                    </button>
                </div>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="w-full text-center py-6 text-xs text-slate-500 border-t border-indigo-900/30 mt-auto">
        <p>by lnwWR.</p>
    </footer>

    <!-- Scratchpad / Drawing Canvas Modal -->
    <div id="scratchpad-modal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center hidden p-2 sm:p-4">
        <div class="bg-slate-900 border border-indigo-900/80 rounded-2xl w-full max-w-4xl h-[90vh] flex flex-col shadow-2xl animate-fade-in overflow-hidden">
            <!-- Modal Header -->
            <div class="flex items-center justify-between px-6 py-4 border-b border-indigo-900/50 bg-slate-950/60">
                <div class="flex items-center space-x-2">
                    <i data-lucide="edit-3" class="w-5 h-5 text-indigo-400"></i>
                    <h3 class="font-bold text-white text-base">กระดาษทดเลข / โน้ตคำนวณ</h3>
                </div>
                <div class="flex items-center space-x-2">
                    <div class="flex bg-slate-800 p-1 rounded-xl text-xs">
                        <button onclick="app.switchScratchMode('draw')" id="mode-draw-btn" class="px-3 py-1.5 rounded-lg bg-indigo-600 text-white font-medium transition-all">โหมดวาดเขียน</button>
                        <button onclick="app.switchScratchMode('text')" id="mode-text-btn" class="px-3 py-1.5 rounded-lg text-slate-300 font-medium transition-all">โหมดพิมพ์โน้ต</button>
                    </div>
                    <button onclick="app.closeScratchpad()" class="p-2 text-slate-400 hover:text-white rounded-xl hover:bg-slate-800 transition-colors">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Modal Body -->
            <div class="flex-grow relative bg-slate-950 overflow-hidden flex flex-col">
                <!-- Draw Canvas View -->
                <div id="scratch-draw-view" class="absolute inset-0 flex flex-col">
                    <div class="flex items-center justify-between px-4 py-2 bg-slate-900/80 border-b border-slate-800 text-xs">
                        <div class="flex items-center space-x-3">
                            <span class="text-slate-400">สีปากกา:</span>
                            <button onclick="app.setPenColor('#ffffff')" class="w-6 h-6 rounded-full bg-white border-2 border-slate-700 focus:outline-none shadow-sm"></button>
                            <button onclick="app.setPenColor('#6366f1')" class="w-6 h-6 rounded-full bg-indigo-500 border-2 border-slate-700 focus:outline-none shadow-sm"></button>
                            <button onclick="app.setPenColor('#fbbf24')" class="w-6 h-6 rounded-full bg-amber-400 border-2 border-slate-700 focus:outline-none shadow-sm"></button>
                            <button onclick="app.setPenColor('#f43f5e')" class="w-6 h-6 rounded-full bg-rose-500 border-2 border-slate-700 focus:outline-none shadow-sm"></button>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="app.clearCanvas()" class="bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 px-3 py-1 rounded-lg border border-rose-500/30 transition-colors flex items-center space-x-1">
                                <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                                <span>ล้างกระดาน</span>
                            </button>
                        </div>
                    </div>
                    <div class="flex-grow relative touch-none bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px]">
                        <canvas id="scratchpad-canvas" class="w-full h-full cursor-crosshair"></canvas>
                    </div>
                </div>

                <!-- Text Note View -->
                <div id="scratch-text-view" class="absolute inset-0 hidden p-4 flex flex-col">
                    <textarea id="scratch-textarea" placeholder="พิมพ์ทดเลข บันทึกสูตร หรือโน้ตเตือนความจำตรงนี้..." class="w-full h-full bg-slate-900/50 border border-slate-800 rounded-xl p-4 text-slate-200 text-sm focus:outline-none focus:border-indigo-500 resize-none font-mono"></textarea>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="px-6 py-3 border-t border-indigo-900/50 bg-slate-950/60 flex justify-between items-center text-xs text-slate-400">
                <span>ใช้เมาส์หรือนิ้วลากบนหน้าจอเพื่อเขียนทดสูตรคำนวณ</span>
                <button onclick="app.closeScratchpad()" class="bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-xl font-medium transition-colors">
                    กลับไปทำโจทย์
                </button>
            </div>
        </div>
    </div>

    <!-- App Logic Script -->
    <script>
        // Question Bank with Natural Thai explanations and correct plain-text SI units and Unicode superscripts
        const questionBank = {
            mechanics: [
                {
                    question: "รถยนต์คันหนึ่งเคลื่อนที่ด้วยความเร็วต้น 10 m/s บนถนนตรง จากนั้นเร่งเครื่องด้วยความเร่งคงที่ 2 m/s² เป็นเวลา 5 s ระยะทางที่รถเคลื่อนที่ได้ในช่วงเวลานี้มีค่าเท่าใด?",
                    options: [
                        "A) 50 เมตร",
                        "B) 75 เมตร",
                        "C) 100 เมตร",
                        "D) 125 เมตร"
                    ],
                    answer: 1,
                    explanation: "ใช้สูตรคำนวณการเคลื่อนที่แนวตรง ระยะทางเท่ากับความเร็วต้นคูณเวลาบวกด้วยเศษหนึ่งส่วนสองคูณความเร่งคูณเวลากำลังสอง แทนค่าจะได้ ระยะทางเท่ากับ 10 คูณ 5 บวกด้วยเศษหนึ่งส่วนสองคูณ 2 คูณ 5² ซึ่งคำนวณออกมาได้เท่ากับ 50 บวก 25 ได้ผลลัพธ์เป็น 75 เมตร"
                },
                {
                    question: "วัตถุวางอยู่บนพื้นราบเกลี้ยง ออกแรงขนาด 20 N ทำมุม 37° กับแนวระดับ ดึงวัตถุมวล 4 kg ให้เคลื่อนที่ไปตามแนวระดับ ความเร่งของวัตถุมีค่าเท่าใด (กำหนดให้ cos 37° = 0.8)",
                    options: [
                        "A) 2.0 m/s²",
                        "B) 3.5 m/s²",
                        "C) 4.0 m/s²",
                        "D) 5.0 m/s²"
                    ],
                    answer: 2,
                    explanation: "จากกฎข้อที่สองของนิวตัน แรงลัพธ์ในแนวระดับเท่ากับมวลคูณความเร่ง แรงดึงในแนวระดับหาได้จากแรงคูณค่า cos 37° แทนค่าจะได้ 20 คูณ 0.8 เท่ากับ 4 คูณความเร่ง จะได้ 16 เท่ากับ 4 คูณความเร่ง ดังนั้นความเร่งมีค่าเท่ากับ 16 หารด้วย 4 ได้ผลลัพธ์เป็น 4.0 m/s²"
                },
                {
                    question: "วัตถุมวล 2 kg ถูกปล่อยให้ตกจากตึกสูง 20 m พลังงานจลน์ของวัตถุก่อนกระทบพื้นดินมีค่าเท่าใด (กำหนดให้ค่าความเร่งโน้มถ่วง g = 10 m/s²)",
                    options: [
                        "A) 200 จูล",
                        "B) 300 จูล",
                        "C) 400 จูล",
                        "D) 500 จูล"
                    ],
                    answer: 2,
                    explanation: "จากกฎการอนุรักษ์พลังงานกล พลังงานศักย์โน้มถ่วงทั้งหมดที่จุดปล่อยจะเปลี่ยนเป็นพลังงานจลน์ก่อนกระทบพื้นพอดี คำนวณได้จากมวลคูณความเร่งโน้มถ่วงคูณความสูง แทนค่าจะได้ 2 คูณ 10 คูณ 20 ได้ผลลัพธ์พลังงานจลน์เท่ากับ 400 จูล"
                },
                {
                    question: "ลูกบอลมวล 0.5 kg เคลื่อนที่ด้วยความเร็ว 10 m/s เข้าชนกำแพงแล้วสะท้อนกลับในแนวเดิมด้วยความเร็ว 6 m/s ใช้เวลาชน 0.1 s แรงเฉลี่ยที่กำแพงกระทำมีค่าเท่าใด?",
                    options: [
                        "A) 40 N",
                        "B) 60 N",
                        "C) 80 N",
                        "D) 100 N"
                    ],
                    answer: 2,
                    explanation: "จากหลักการการดลและโมเมนตัม แรงเฉลี่ยคูณเวลาที่ชนเท่ากับผลต่างของโมเมนตัม แทนค่ามวลและผลต่างความเร็ว คือ 0.5 คูณด้วยผลต่างระหว่างความเร็วปลายกับความเร็วต้น หารด้วยเวลา 0.1 s คำนวณแรงเฉลี่ยออกมาได้เท่ากับ 80 N"
                },
                {
                    question: "ดาวเทียมดวงหนึ่งโคจรด้วยรัศมี R และอัตราเร็ว v หากย้ายไปโคจรที่รัศมี 4R อัตราเร็วในการโคจรใหม่จะมีค่าเป็นกี่เท่าของเดิม?",
                    options: [
                        "A) 0.5v",
                        "B) 2v",
                        "C) 4v",
                        "D) 0.25v"
                    ],
                    answer: 0,
                    explanation: "จากสูตรความเร็วในการโคจรรอบโลก อัตราเร็วจะแปรผกผันกับรากที่สองของรัศมีวงโคจร เมื่อรัศมีเพิ่มขึ้นเป็น 4 เท่า อัตราเร็วจึงลดลงเหลือเศษหนึ่งส่วนรากที่สองของ 4 ซึ่งเท่ากับ 0.5 เท่าของความเร็วเดิม"
                }
            ],
            electricity: [
                {
                    question: "ประจุไฟฟ้า q₁ = +2 μC และ q₂ = -8 μC ห่างกัน 6 cm ตำแหน่งที่สนามไฟฟ้าลัพธ์เป็นศูนย์อยู่ห่างจากประจุ q₁ เท่าใด?",
                    options: [
                        "A) 2 เซนติเมตร",
                        "B) 4 เซนติเมตร",
                        "C) 6 เซนติเมตร",
                        "D) 8 เซนติเมตร"
                    ],
                    answer: 2,
                    explanation: "จุดที่สนามไฟฟ้าเป็นศูนย์จะต้องอยู่ด้านนอกและใกล้กับประจุที่มีค่าน้อยกว่า ตั้งสมการสนามไฟฟ้าจากประจุทั้งสองให้เท่ากัน แก้สมการหาคำตอบจะได้ระยะห่างจากประจุ q₁ เท่ากับ 6 cm พอดี"
                },
                {
                    question: "ลวดตัวนำยาว L มีความต้านทาน R รีดลวดใหม่ให้ยาวเป็น 2 เท่าโดยปริมาตรคงเดิม ความต้านทานใหม่จะเป็นกี่เท่าของเดิม?",
                    options: [
                        "A) 2 เท่า",
                        "B) 4 เท่า",
                        "C) 8 เท่า",
                        "D) 16 เท่า"
                    ],
                    answer: 1,
                    explanation: "จากสูตรความต้านทานแปรผันตรงกับความยาวและแปรผกผันกับพื้นที่หน้าตัด เมื่อยืดลวดให้ยาวขึ้นเป็น 2 เท่าโดยปริมาตรไม่เปลี่ยน พื้นที่หน้าตัดจะลดลงครึ่งหนึ่ง ส่งผลให้ความต้านทานเพิ่มขึ้นเป็น 4 เท่า"
                },
                {
                    question: "วงจรไฟฟ้ามีแรงเคลื่อนไฟฟ้า 12 V ความต้านทานภายใน 1 ohm ต่ออนุกรมกับตัวต้านทาน 5 ohm กระแสไฟฟ้าในวงจรมีค่าเท่าใด?",
                    options: [
                        "A) 1.5 A",
                        "B) 2.0 A",
                        "C) 2.4 A",
                        "D) 3.0 A"
                    ],
                    answer: 1,
                    explanation: "จากกฎของโอห์มสำหรับวงจรไฟฟ้า กระแสไฟฟ้าหาได้จากแรงเคลื่อนไฟฟ้าหารด้วยผลบวกของความต้านทานภายนอกและภายใน แทนค่าจะได้ 12 หารด้วย 5 บวก 1 ได้ผลลัพธ์กระแสไฟฟ้าเท่ากับ 2.0 A"
                },
                {
                    question: "อนุภาคประจุบวกเคลื่อนที่ตั้งฉากกับสนามแม่เหล็กสม่ำเสมอ รัศมีวงโคจรแปรผันตรงกับตัวแปรใดมากที่สุด?",
                    options: [
                        "A) มวลและประจุไฟฟ้า",
                        "B) มวลและความเร็ว",
                        "C) ความเข้มสนามแม่เหล็ก",
                        "D) พลังงานจลน์"
                    ],
                    answer: 1,
                    explanation: "จากสูตรการเคลื่อนที่ของประจุในสมการรัศมีวงโคจร รัศมีจะเท่ากับมวลคูณความเร็วหารด้วยประจุคูณสนามแม่เหล็ก ดังนั้นรัศมีจึงแปรผันตรงกับมวลและอัตราเร็วของอนุภาค"
                },
                {
                    question: "หม้อแปลงไฟฟ้าในอุดมคติ ขดลวดปฐมภูมิ 200 รอบ ขดลวดทุติยภูมิ 800 รอบ ป้อนแรงดันไฟฟ้า 50 V แรงดันไฟฟ้าฝั่งทุติยภูมิคือเท่าใด?",
                    options: [
                        "A) 100 V",
                        "B) 150 V",
                        "C) 200 V",
                        "D) 400 V"
                    ],
                    answer: 2,
                    explanation: "จากอัตราส่วนแรงดันไฟฟ้าเท่ากับอัตราส่วนจำนวนรอบของขดลวดหม้อแปลง แทนค่าจะได้แรงดันฝั่งทุติยภูมิเท่ากับ 50 คูณด้วย 800 หารด้วย 200 ได้ผลลัพธ์เป็น 200 V"
                }
            ],
            waves: [
                {
                    question: "คลื่นดลในเส้นเชือกมีอัตราเร็ว 20 m/s ความถี่ 5 Hz ระยะห่างระหว่างจุดที่มีเฟสตรงกันและอยู่ใกล้กันที่สุดมีค่าเท่าใด?",
                    options: [
                        "A) 2 เมตร",
                        "B) 4 เมตร",
                        "C) 5 เมตร",
                        "D) 10 เมตร"
                    ],
                    answer: 1,
                    explanation: "คำนวณความยาวคลื่นจากอัตราเร็วคลื่นหารด้วยความถี่ จะได้ 20 หารด้วย 5 เท่ากับ 4 เมตร ระยะห่างระหว่างจุดที่มีเฟสตรงกันที่อยู่ใกล้ที่สุดจะเท่ากับหนึ่งความยาวคลื่นพอดี คือ 4 เมตร"
                },
                {
                    question: "แหล่งกำเนิดเสียงมีความถี่ 680 Hz อัตราเร็วเสียงในอากาศ 340 m/s ความยาวคลื่นเสียงในอากาศมีค่าเท่าใด?",
                    options: [
                        "A) 0.25 เมตร",
                        "B) 0.50 เมตร",
                        "C) 1.00 เมตร",
                        "D) 2.00 เมตร"
                    ],
                    answer: 1,
                    explanation: "ความยาวคลื่นเสียงหาได้จากอัตราเร็วเสียงในอากาศหารด้วยความถี่ แทนค่าจะได้ 340 หารด้วย 680 ได้ผลลัพธ์ความยาวคลื่นเท่ากับ 0.50 เมตร"
                },
                {
                    question: "การทดลองการแทรกสอดสลิตคู่ยัง ความยาวคลื่นแสง 500 nm ระยะห่างระหว่างสลิต 0.2 mm ฉากอยู่ห่าง 1 m ระยะห่างระหว่างแถบสว่างติดกันเท่าใด?",
                    options: [
                        "A) 1.5 มิลลิเมตร",
                        "B) 2.0 มิลลิเมตร",
                        "C) 2.5 มิลลิเมตร",
                        "D) 3.0 มิลลิเมตร"
                    ],
                    answer: 2,
                    explanation: "จากสูตรระยะห่างระหว่างแถบสว่างในการทดลองสลิตคู่ นำความยาวคลื่นคูณระยะฉากแล้วหารด้วยระยะห่างระหว่างสลิต แทนค่าหน่วยเป็นเมตร จะคำนวณระยะห่างระหว่างแถบสว่างได้เท่ากับ 2.5 มิลลิเมตร"
                },
                {
                    question: "วางวัตถุไว้หน้ากระจกเว้ามีความยาวโฟกัส 15 cm ที่ระยะ 30 cm ภาพที่เกิดขึ้นมีลักษณะอย่างไร?",
                    options: [
                        "A) ภาพจริง หัวตั้ง ขนาดเท่าวัตถุ",
                        "B) ภาพจริง หัวกลับ ขนาดเท่าวัตถุ",
                        "C) ภาพเสมือน หัวตั้ง ขนาดใหญ่กว่าวัตถุ",
                        "D) ภาพจริง หัวกลับ ขนาดใหญ่กว่าวัตถุ"
                    ],
                    answer: 1,
                    explanation: "คำนวณระยะภาพจากสูตรกระจกโค้ง เมื่อวางวัตถุที่ระยะ 2 เท่าของความยาวโฟกัส ภาพจริงจะเกิดขึ้นที่ระยะ 2 เท่าเช่นกัน โดยเป็นภาพจริงหัวกลับและมีขนาดเท่ากับวัตถุพอดี"
                },
                {
                    question: "เงื่อนไขข้อใดทำให้เกิดการเลี้ยวเบนของคลื่นผ่านช่องเปิดแคบได้ดีที่สุด?",
                    options: [
                        "A) ช่องเปิดกว้างกว่าความยาวคลื่นมากๆ",
                        "B) ความยาวคลื่นน้อยกว่าช่องเปิดมากๆ",
                        "C) ขนาดของช่องเปิดมีค่าใกล้เคียงกับความยาวคลื่น",
                        "D) ความถี่คลื่นมีค่าสูงขึ้นเรื่อยๆ"
                    ],
                    answer: 2,
                    explanation: "ปรากฏการณ์การเลี้ยวเบนของคลื่นจะเกิดขึ้นได้ดีและสังเกตได้ชัดเจน เมื่อขนาดของช่องเปิดหรือสิ่งกีดขวางมีค่าใกล้เคียงหรือน้อยกว่าความยาวคลื่นที่มากระทบ"
                }
            ],
            modern: [
                {
                    question: "ฟังก์ชันงานของโลหะชนิดหนึ่งเท่ากับ 2.0 eV ฉายแสงที่มีพลังงาน 3.5 eV มากระทบ พลังงานจลน์สูงสุดของโฟโตอิเล็กตรอนมีค่าเท่าใด?",
                    options: [
                        "A) 1.5 eV",
                        "B) 2.0 eV",
                        "C) 3.5 eV",
                        "D) 5.5 eV"
                    ],
                    answer: 0,
                    explanation: "จากสมการโฟโตอิเล็กทริก พลังงานจลน์สูงสุดของอิเล็กตรอนหาได้จากพลังงานของโฟตอนลบด้วยฟังก์ชันงานของโลหะ แทนค่าจะได้ 3.5 ลบด้วย 2.0 เท่ากับ 1.5 eV"
                },
                {
                    question: "รัศมีวงโคจรอิเล็กตรอนตามแบบของโบร์ในวงโคจรชั้น n = 3 เป็นกี่เท่าของสถานะพื้นชั้น n = 1?",
                    options: [
                        "A) 3 เท่า",
                        "B) 6 เท่า",
                        "C) 9 เท่า",
                        "D) 27 เท่า"
                    ],
                    answer: 2,
                    explanation: "จากทฤษฎีอะตอมของโบร์ รัศมีวงโคจรแปรผันตามกำลังสองของเลขควอนตัมหลัก เมื่อชั้น n = 3 รัศมีจะเพิ่มขึ้นเป็น 3² ซึ่งเท่ากับ 9 เท่าของสถานะพื้น"
                },
                {
                    question: "ธาตุกัมมันตรังสีมีครึ่งชีวิต 8 วัน เริ่มต้นมีสารนี้อยู่ 80 g ผ่านไป 24 วัน จะเหลือสารนี้อยู่กี่กรัม?",
                    options: [
                        "A) 5 กรัม",
                        "B) 10 กรัม",
                        "C) 20 กรัม",
                        "D) 40 กรัม"
                    ],
                    answer: 1,
                    explanation: "คำนวณจำนวนครึ่งชีวิตโดยนำเวลาทั้งหมดหารด้วยครึ่งชีวิต ได้ 24 หารด้วย 8 เท่ากับ 3 ช่วงครึ่งชีวิต นำปริมาณเริ่มต้นมาคูณด้วยเศษหนึ่งส่วนสองยกกำลังสาม จะได้ 80 คูณเศษหนึ่งส่วนแปด ได้ผลลัพธ์เหลือ 10 กรัม"
                },
                {
                    question: "ยานอวกาศเคลื่อนที่ด้วยความเร็ว 0.6c นาฬิกาบนยานเดินผ่านไป 10 นาที เวลาบนโลกจะผ่านไปนานเท่าใด?",
                    options: [
                        "A) 8 นาที",
                        "B) 10 นาที",
                        "C) 12.5 นาที",
                        "D) 16.6 นาที"
                    ],
                    answer: 2,
                    explanation: "จากทฤษฎีสัมพัทธภาพพิเศษ เวลาบนโลกจะเดินช้ากว่าหรือเรียกว่าการยืดออกของเวลา คำนวณโดยนำเวลาบนยานหารด้วยแฟกเตอร์ลอเรนทซ์ แทนค่าจะได้ 10 หารด้วย 0.8 ได้ผลลัพธ์เท่ากับ 12.5 นาที"
                },
                {
                    question: "ปฏิกิริยานิวเคลียร์ที่เกิดขึ้นบนดวงอาทิตย์ซึ่งให้พลังงานมหาศาล คือปฏิกิริยาในข้อใด?",
                    options: [
                        "A) นิวเคลียร์ฟิชชันของยูเรเนียม",
                        "B) การสลายให้รังสีบีตาของคาร์บอน",
                        "C) นิวเคลียร์ฟิวชันของการรวมตัวของไฮโดรเจน",
                        "D) การแตกตัวของสารกัมมันตรังสี"
                    ],
                    answer: 2,
                    explanation: "พลังงานบนดวงอาทิตย์เกิดจากปฏิกิริยานิวเคลียร์ฟิวชัน ซึ่งเป็นการหลอมรวมนิวเคลียสของไฮโดรเจนให้กลายเป็นฮีเลียมและปลดปล่อยพลังงานความร้อนและแสงสว่างออกมา"
                }
            ],
            fluids: [
                {
                    question: "เขื่อนกักเก็บน้ำมีความลึก 20 m ความดันเกจที่ก้นเขื่อนมีค่าเท่าใด (กำหนดความหนาแน่นน้ำ 1000 kg/m³, ความเร่งโน้มถ่วง g = 10 m/s²)",
                    options: [
                        "A) 1.0 × 10⁵ Pa",
                        "B) 2.0 × 10⁵ Pa",
                        "C) 3.0 × 10⁵ Pa",
                        "D) 4.0 × 10⁵ Pa"
                    ],
                    answer: 1,
                    explanation: "จากสูตรความดันเกจในของเหลว ความดันเท่ากับความหนาแน่นคูณความเร่งโน้มถ่วงคูณความลึก แทนค่าจะได้ 1000 คูณ 10 คูณ 20 ได้ผลลัพธ์เป็น 2.0 × 10⁵ Pa"
                },
                {
                    question: "วัตถุก้อนหนึ่งลอยน้ำโดยมีปริมาตรจมอยู่ 80% ของปริมาตรทั้งหมด ความหนาแน่นของวัตถุก้อนนี้มีค่าเท่าใด (ความหนาแน่นน้ำ 1000 kg/m³)",
                    options: [
                        "A) 200 kg/m³",
                        "B) 400 kg/m³",
                        "C) 600 kg/m³",
                        "D) 800 kg/m³"
                    ],
                    answer: 3,
                    explanation: "จากสมดุลแรงลอยตัวและน้ำหนักวัตถุ อัตราส่วนปริมาตรส่วนที่จมต่อปริมาตรทั้งหมดจะเท่ากับอัตราส่วนความหนาแน่นของวัตถุต่อน้ำ ดังนั้นความหนาแน่นวัตถุจึงเท่ากับ 0.8 คูณ 1000 ได้ 800 kg/m³"
                },
                {
                    question: "ท่อประปามีพื้นที่หน้าตัด 4 cm² น้ำไหลด้วยอัตราเร็ว 2 m/s หากท่อแคบลงเหลือพื้นที่หน้าตัด 1 cm² อัตราเร็วของน้ำในส่วนที่แคบจะเป็นเท่าใด?",
                    options: [
                        "A) 2 m/s",
                        "B) 4 m/s",
                        "C) 6 m/s",
                        "D) 8 m/s"
                    ],
                    answer: 3,
                    explanation: "จากสมการความต่อเนื่องของของไหล พื้นที่หน้าตัดคูณอัตราเร็วที่จุดแรกเท่ากับที่จุดหลัง แทนค่าจะได้ 4 คูณ 2 เท่ากับ 1 คูณอัตราเร็วใหม่ คำนวณได้อัตราเร็วเท่ากับ 8 m/s"
                },
                {
                    question: "ข้อใดกล่าวถึงกฎของพาสคาลได้ถูกต้องที่สุด?",
                    options: [
                        "A) ความดันในของเหลวขึ้นอยู่กับความลึกเท่านั้น",
                        "B) ความดันที่กระทำต่อของเหลวในภาชนะปิดจะถูกถ่ายเทไปทุกทิศทางเท่ากัน",
                        "C) แรงพยุงของของเหลวเท่ากับน้ำหนักของของเหลวที่ถูกแทนที่",
                        "D) อัตราเร็วของของไหลเพิ่มขึ้น ความดันจะลดลง"
                    ],
                    answer: 1,
                    explanation: "กฎของพาสคาลอธิบายว่า เมื่อเพิ่มความดันให้กับของเหลวที่อยู่นิ่งในภาชนะปิด ความดันนั้นจะถูกถ่ายทอดไปยังทุกๆ จุดของของเหลวโดยมีขนาดเท่ากันทั้งหมด"
                },
                {
                    question: "หลอดแก้วรูปร่างเล็กมากจุ่มในน้ำแล้วระดับน้ำสูงขึ้น ปรากฏการณ์นี้เกิดจากแรงใดเป็นหลัก?",
                    options: [
                        "A) แรงพยุงของน้ำ",
                        "B) ความดันบรรยากาศ",
                        "C) แรงตึงผิวและแรงยึดติดระหว่างน้ำกับผิวแก้ว",
                        "D) ความหนืดของของเหลว"
                    ],
                    answer: 2,
                    explanation: "การที่ของเหลวไต่ระดับสูงขึ้นในหลอดแก้วเล็กเรียกว่าคาปิลลารีแอกชัน ซึ่งเกิดจากแรงตึงผิวของของเหลวร่วมกับแรงยึดติดระหว่างโมเลกุลของน้ำกับผิวแก้ว"
                }
            ],
            thermo: [
                {
                    question: "อุณหภูมิของร่างกายผู้ป่วยวัดได้ 40 °C อุณหภูมินี้จะมีค่าเท่าใดในหน่วย Fahrenheit?",
                    options: [
                        "A) 98.6 °F",
                        "B) 104.0 °F",
                        "C) 107.6 °F",
                        "D) 112.0 °F"
                    ],
                    answer: 1,
                    explanation: "จากสูตรแปลงหน่วยอุณหภูมิระหว่างเซลเซียสและฟาเรนไฮต์ แทนค่า 40 °C ลงในสูตร จะคำนวณอุณหภูมิในหน่วยฟาเรนไฮต์ได้เท่ากับ 104.0 °F พอดี"
                },
                {
                    question: "ให้ความร้อน 2100 J แก่น้ำแข็งมวล 5 g ที่ 0 °C จนหลอมเหลวเป็นน้ำหมดพอดี ความร้อนแฝงของการหลอมเหลวของน้ำมีค่าเท่าใด?",
                    options: [
                        "A) 333 J/g",
                        "B) 420 J/g",
                        "C) 500 J/g",
                        "D) 600 J/g"
                    ],
                    answer: 1,
                    explanation: "จากสูตรความร้อนในการเปลี่ยนสถานะ ความร้อนแฝงเท่ากับปริมาณความร้อนหารด้วยมวล แทนค่าจะได้ 2100 J หารด้วย 5 g ได้ผลลัพธ์เท่ากับ 420 J/g"
                },
                {
                    question: "แก๊สอุดมคติปริมาตร 2 L ที่ความดัน 3 บรรยากาศ ถูกอัดให้มีปริมาตรเหลือ 1 L โดยอุณหภูมิคงที่ ความดันใหม่จะเป็นเท่าใด?",
                    options: [
                        "A) 1.5 บรรยากาศ",
                        "B) 3.0 บรรยากาศ",
                        "C) 4.5 บรรยากาศ",
                        "D) 6.0 บรรยากาศ"
                    ],
                    answer: 3,
                    explanation: "จากกฎของบอยล์เมื่ออุณหภูมิคงที่ ผลคูณของความดันกับปริมาตรเริ่มต้นจะเท่ากับตอนหลัง แทนค่าจะได้ 3 คูณ 2 เท่ากับความดันใหม่คูณ 1 คำนวณได้ความดันใหม่เป็น 6 บรรยากาศ"
                },
                {
                    question: "พลังงานจลน์เฉลี่ยของโมเลกุลแก๊สอุดมคติขึ้นอยู่กับตัวแปรใดมากที่สุด?",
                    options: [
                        "A) ปริมาตรของแก๊ส",
                        "B) ความดันของแก๊ส",
                        "C) อุณหภูมิสัมบูรณ์ในหน่วยเคลวิน",
                        "D) ชนิดของโมเลกุลแก๊ส"
                    ],
                    answer: 2,
                    explanation: "ตามทฤษฎีจลน์ของแก๊ส พลังงานจลน์เฉลี่ยของโมเลกุลแก๊สจะแปรผันตรงกับอุณหภูมิสัมบูรณ์ในหน่วยเคลวินของแก๊สนั้นๆ เท่านั้น"
                },
                {
                    question: "ตามกฎข้อที่หนึ่งของอุณหพลศาสตร์ ระบบได้รับความร้อน 500 J และมีการทำงานออกจากระบบ 200 J พลังงานภายในระบบเปลี่ยนไปอย่างไร?",
                    options: [
                        "A) เพิ่มขึ้น 300 J",
                        "B) ลดลง 300 J",
                        "C) เพิ่มขึ้น 700 J",
                        "D) ลดลง 700 J"
                    ],
                    answer: 0,
                    explanation: "จากกฎข้อที่หนึ่งการเปลี่ยนแปลงพลังงานภายในระบบเท่ากับความร้อนที่ได้รับลบด้วยงานที่ระบบทำออกไป แทนค่าจะได้ 500 J ลบด้วย 200 J ได้ผลลัพธ์พลังงานภายในเพิ่มขึ้น 300 J"
                }
            ],
            challenge: [
                {
                    question: "ชาเลนจ์ข้อที่ 1: วัตถุมวล 5 kg ถูกยิงด้วยปืนใหญ่ทำให้เคลื่อนที่ขึ้นไปตามพื้นเอียง 30° ด้วยความเร็วต้น 20 m/s สัมประสิทธิ์ความเสียดทานจลน์เท่ากับ 0.2 ระยะทางสูงสุดที่วัตถุเคลื่อนที่ขึ้นไปตามพื้นเอียงได้มีค่าเท่าใด (กำหนดให้ค่า g = 10 m/s²)",
                    options: [
                        "A) 12.5 เมตร",
                        "B) 15.2 เมตร",
                        "C) 18.6 เมตร",
                        "D) 22.4 เมตร"
                    ],
                    answer: 1,
                    explanation: "โจทย์ข้อนี้ต้องใช้หลักงานและพลังงานร่วมกับแรงเสียดทาน งานของแรงภายนอกและแรงเสียดทานเท่ากับพลังงานกลรวมที่เปลี่ยนไป คิดแรงเสียดทานและแรงโน้มถ่วงที่ต้านการเคลื่อนที่แล้วแก้สมการหาระยะทาง จะได้ระยะทางประมาณ 15.2 เมตร"
                },
                {
                    question: "ชาเลนจ์ข้อที่ 2: วงจรไฟฟ้ากระแสสลับประกอบด้วยตัวต้านทาน 30 ohm ขดลวดเหนี่ยวนำ 40 ohm ต่ออนุกรมกันด้วยแหล่งจ่ายไฟฟ้า 220 V ความถี่ 50 Hz กระแสไฟฟ้าสูงสุดในวงจรมีค่าเท่าใด?",
                    options: [
                        "A) 2.2 แอมแปร์",
                        "B) 3.1 แอมแปร์",
                        "C) 4.4 แอมแปร์",
                        "D) 6.2 แอมแปร์"
                    ],
                    answer: 2,
                    explanation: "หาความต้านทานเชิงซ้อนหรืออิมพีแดนซ์รวมของวงจรจากรากที่สองของผลบวกกำลังสองของความต้านทานและรีแอกแตนซ์เหนี่ยวนำ จะได้ 50 ohm จากนั้นนำแรงดันสูงสุดหารด้วยอิมพีแดนซ์ จะได้กระแสสูงสุด 4.4 แอมแปร์"
                },
                {
                    question: "ชาเลนจ์ข้อที่ 3: แหล่งกำเนิดคลื่นสองแหล่งเฟสตรงกันห่างกัน 12 cm ความยาวคลื่น 3 cm จุดที่อยู่บนเส้นตรงระหว่างแหล่งกำเนิดทั้งสองและอยู่ห่างจากแหล่งแรก 4.5 cm จะอยู่บนแนวปฏิบัตรหรือบัตรที่เท่าใด?",
                    options: [
                        "A) บัตรที่ 1",
                        "B) ปฏิบัตรที่ 2",
                        "C) บัตรที่ 2",
                        "D) ปฏิบัตรที่ 3"
                    ],
                    answer: 2,
                    explanation: "คำนวณระยะทางจากแหล่งกำเนิดทั้งสองไปยังจุดนั้น ได้ระยะทาง 4.5 cm และ 7.5 cm หาผลต่างระยะทางได้ 3 cm ซึ่งเท่ากับหนึ่งความยาวคลื่นพอดี ทำให้ทราบว่าเป็นตำแหน่งของบัตรที่ 2"
                },
                {
                    question: "ชาเลนจ์ข้อที่ 4: อนุกรมสเปกตรัมไฮโดรเจนในอนุกรมพาสเชน เส้นที่มีความยาวคลื่นสั้นที่สุดมีค่าประมาณกี่นาโนเมตร (กำหนดค่าคงที่ริดเบิร์ก R = 1.097 × 10⁷ m⁻¹)",
                    options: [
                        "A) 656 นาโนเมตร",
                        "B) 820 นาโนเมตร",
                        "C) 1215 นาโนเมตร",
                        "D) 1875 นาโนเมตร"
                    ],
                    answer: 3,
                    explanation: "อนุกรมพาสเชนมีระดับพลังงานต่ำสุด n = 3 และความยาวคลื่นสั้นที่สุดเกิดขึ้นเมื่ออิเล็กตรอนตกลงมาจากระดับอนันต์ (infinity) แทนค่าในสมการริดเบิร์กจะได้ความยาวคลื่นประมาณ 1875 nm"
                },
                {
                    question: "ชาเลนจ์ข้อที่ 5: ท่อปลายเปิดสองข้างยาว 1.5 m เกิดการสั่นพ้องของเสียงในฮาร์มอนิกที่ 2 อัตราเร็วเสียงในอากาศ 340 m/s ความถี่ของเสียงนี้มีค่าเท่าใด?",
                    options: [
                        "A) 113.3 Hz",
                        "B) 226.7 Hz",
                        "C) 340.0 Hz",
                        "D) 453.3 Hz"
                    ],
                    answer: 1,
                    explanation: "สำหรับท่อปลายเปิดสองข้าง ความถี่ฮาร์มอนิกที่ n หาได้จาก n คูณอัตราเร็วเสียงหารด้วยสองเท่าของความยาวท่อ แทนค่า n = 2 ความเร็ว 340 และความยาว 1.5 m จะคำนวณความถี่ได้ 226.7 Hz"
                }
            ]
        };

        // App State
        let appState = {
            currentCategory: 'all',
            selectedCount: 5,
            selectedTimerMinutes: 15,
            activeQuestions: [],
            currentIndex: 0,
            score: 0,
            timeLeft: 900,
            isTimerPaused: false,
            timerInterval: null,
            userAnswers: [],
            scratchMode: 'draw',
            penColor: '#ffffff',
            isDrawing: false,
            lastX: 0,
            lastY: 0
        };

        const app = {
            setQuestionCount(count) {
                appState.selectedCount = count;
                [5, 10, 20, 30, 'all'].forEach(c => {
                    const btn = document.getElementById(`count-btn-${c}`);
                    if (btn) {
                        if (c === count) {
                            btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-indigo-600 text-white shadow-md shadow-indigo-600/30";
                        } else {
                            btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700";
                        }
                    }
                });
            },

            setTimerDuration(mins) {
                appState.selectedTimerMinutes = mins;
                [15, 30, 45, 60].forEach(m => {
                    const btn = document.getElementById(`timer-btn-${m}`);
                    if (btn) {
                        if (m === mins) {
                            btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-indigo-600 text-white shadow-md shadow-indigo-600/30";
                        } else {
                            btn.className = "px-3 py-1.5 rounded-xl text-xs font-medium transition-all bg-slate-800 text-slate-300 hover:bg-slate-700";
                        }
                    }
                });
            },

            startQuiz(category) {
                appState.currentCategory = category;
                appState.currentIndex = 0;
                appState.score = 0;
                appState.timeLeft = appState.selectedTimerMinutes * 60;
                appState.isTimerPaused = false;
                appState.userAnswers = [];

                let pool = [];
                if (category === 'all') {
                    pool = [
                        ...questionBank.mechanics,
                        ...questionBank.electricity,
                        ...questionBank.waves,
                        ...questionBank.modern,
                        ...questionBank.fluids,
                        ...questionBank.thermo,
                        ...questionBank.challenge
                    ];
                } else {
                    pool = [...(questionBank[category] || questionBank.mechanics)];
                }

                pool.sort(() => Math.random() - 0.5);
                if (appState.selectedCount !== 'all' && pool.length > appState.selectedCount) {
                    appState.activeQuestions = pool.slice(0, appState.selectedCount);
                } else {
                    appState.activeQuestions = pool;
                }

                document.getElementById('screen-home').classList.add('hidden');
                document.getElementById('screen-result').classList.add('hidden');
                document.getElementById('screen-quiz').classList.remove('hidden');

                const categoryNames = {
                    mechanics: 'กลศาสตร์',
                    electricity: 'ไฟฟ้าและแม่เหล็ก',
                    waves: 'คลื่นและแสง',
                    modern: 'ฟิสิกส์ยุคใหม่',
                    fluids: 'ของไหลและความตึงผิว',
                    thermo: 'ความร้อนและแก๊ส',
                    challenge: 'โหมดชาเลนจ์พิเศษ (⚡)',
                    all: 'รวมทุกหมวดหมู่'
                };
                document.getElementById('nav-category-badge').innerText = categoryNames[category];

                if (appState.timerInterval) clearInterval(appState.timerInterval);
                this.updateTimerDisplay();
                appState.timerInterval = setInterval(() => {
                    if (!appState.isTimerPaused) {
                        if (appState.timeLeft > 0) {
                            appState.timeLeft--;
                            this.updateTimerDisplay();
                        } else {
                            clearInterval(appState.timerInterval);
                            this.showResults();
                        }
                    }
                }, 1000);

                this.loadQuestion();
            },

            updateTimerDisplay() {
                const mins = String(Math.floor(appState.timeLeft / 60)).padStart(2, '0');
                const secs = String(appState.timeLeft % 60).padStart(2, '0');
                document.getElementById('quiz-timer').innerText = `${mins}:${secs}`;
            },

            toggleTimer() {
                appState.isTimerPaused = !appState.isTimerPaused;
                const icon = document.getElementById('timer-icon');
                const btn = document.getElementById('timer-pause-btn');
                if (appState.isTimerPaused) {
                    icon.setAttribute('data-lucide', 'play');
                    btn.title = "เล่นเวลาต่อ";
                    btn.className = "text-xs text-emerald-400 hover:text-white bg-emerald-500/10 hover:bg-emerald-500/20 px-2 py-1.5 rounded-xl transition-colors flex items-center justify-center";
                } else {
                    icon.setAttribute('data-lucide', 'pause');
                    btn.title = "หยุดเวลาชั่วคราว";
                    btn.className = "text-xs text-amber-400 hover:text-white bg-amber-500/10 hover:bg-amber-500/20 px-2 py-1.5 rounded-xl transition-colors flex items-center justify-center";
                }
                lucide.createIcons();
            },

            resetTimer() {
                appState.timeLeft = appState.selectedTimerMinutes * 60;
                appState.isTimerPaused = false;
                this.updateTimerDisplay();
                const icon = document.getElementById('timer-icon');
                const btn = document.getElementById('timer-pause-btn');
                icon.setAttribute('data-lucide', 'pause');
                btn.title = "หยุดเวลาชั่วคราว";
                btn.className = "text-xs text-amber-400 hover:text-white bg-amber-500/10 hover:bg-amber-500/20 px-2 py-1.5 rounded-xl transition-colors flex items-center justify-center";
                lucide.createIcons();
            },

            openScratchpad() {
                document.getElementById('scratchpad-modal').classList.remove('hidden');
                setTimeout(() => {
                    this.initCanvas();
                }, 100);
            },

            closeScratchpad() {
                document.getElementById('scratchpad-modal').classList.add('hidden');
            },

            switchScratchMode(mode) {
                appState.scratchMode = mode;
                const drawBtn = document.getElementById('mode-draw-btn');
                const textBtn = document.getElementById('mode-text-btn');
                const drawView = document.getElementById('scratch-draw-view');
                const textView = document.getElementById('scratch-text-view');

                if (mode === 'draw') {
                    drawBtn.className = "px-3 py-1.5 rounded-lg bg-indigo-600 text-white font-medium transition-all";
                    textBtn.className = "px-3 py-1.5 rounded-lg text-slate-300 font-medium transition-all";
                    drawView.classList.remove('hidden');
                    textView.classList.add('hidden');
                    this.initCanvas();
                } else {
                    textBtn.className = "px-3 py-1.5 rounded-lg bg-indigo-600 text-white font-medium transition-all";
                    drawBtn.className = "px-3 py-1.5 rounded-lg text-slate-300 font-medium transition-all";
                    textView.classList.remove('hidden');
                    drawView.classList.add('hidden');
                }
            },

            initCanvas() {
                const canvas = document.getElementById('scratchpad-canvas');
                if (!canvas) return;
                const ctx = canvas.getContext('2d');
                
                const rect = canvas.getBoundingClientRect();
                if (canvas.width !== rect.width || canvas.height !== rect.height) {
                    canvas.width = rect.width;
                    canvas.height = rect.height;
                    ctx.fillStyle = '#020617';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                }

                canvas.onmousedown = null;
                canvas.onmousemove = null;
                canvas.onmouseup = null;

                const getPos = (e) => {
                    const r = canvas.getBoundingClientRect();
                    const clientX = e.clientX || (e.touches && e.touches[0].clientX);
                    const clientY = e.clientY || (e.touches && e.touches[0].clientY);
                    return {
                        x: clientX - r.left,
                        y: clientY - r.top
                    };
                };

                const startDraw = (e) => {
                    e.preventDefault();
                    appState.isDrawing = true;
                    const pos = getPos(e);
                    appState.lastX = pos.x;
                    appState.lastY = pos.y;
                };

                const draw = (e) => {
                    if (!appState.isDrawing) return;
                    e.preventDefault();
                    const pos = getPos(e);
                    ctx.beginPath();
                    ctx.moveTo(appState.lastX, appState.lastY);
                    ctx.lineTo(pos.x, pos.y);
                    ctx.strokeStyle = appState.penColor;
                    ctx.lineWidth = 3;
                    ctx.lineCap = 'round';
                    ctx.lineJoin = 'round';
                    ctx.stroke();
                    appState.lastX = pos.x;
                    appState.lastY = pos.y;
                };

                const stopDraw = (e) => {
                    appState.isDrawing = false;
                };

                canvas.onmousedown = startDraw;
                canvas.onmousemove = draw;
                canvas.onmouseup = stopDraw;
                canvas.onmouseleave = stopDraw;

                canvas.ontouchstart = startDraw;
                canvas.ontouchmove = draw;
                canvas.ontouchend = stopDraw;
            },

            setPenColor(color) {
                appState.penColor = color;
            },

            clearCanvas() {
                const canvas = document.getElementById('scratchpad-canvas');
                const ctx = canvas.getContext('2d');
                ctx.fillStyle = '#020617';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
            },

            loadQuestion() {
                const q = appState.activeQuestions[appState.currentIndex];
                const total = appState.activeQuestions.length;

                document.getElementById('quiz-progress-text').innerText = `คำถามที่ ${appState.currentIndex + 1} จาก ${total}`;
                document.getElementById('quiz-category-label').innerText = this.getCategoryName(appState.currentCategory);
                const progressPercent = ((appState.currentIndex) / total) * 100;
                document.getElementById('quiz-progress-bar').style.width = `${progressPercent}%`;

                document.getElementById('question-text').innerHTML = q.question;

                const optionsContainer = document.getElementById('options-container');
                optionsContainer.innerHTML = '';

                q.options.forEach((opt, idx) => {
                    const btn = document.createElement('button');
                    btn.className = "w-full text-left p-4 rounded-xl border border-slate-800 bg-slate-950/60 hover:bg-slate-800/80 hover:border-indigo-500/50 transition-all text-slate-200 text-sm font-medium flex items-center justify-between group";
                    btn.innerHTML = `
                        <span>${opt}</span>
                        <span class="w-6 h-6 rounded-full border border-slate-700 flex items-center justify-center text-xs text-slate-500 group-hover:border-indigo-400 group-hover:text-indigo-300 transition-colors">${String.fromCharCode(65 + idx)}</span>
                    `;
                    btn.onclick = () => this.selectOption(idx);
                    optionsContainer.appendChild(btn);
                });

                document.getElementById('explanation-box').classList.add('hidden');
                document.getElementById('action-container').classList.add('hidden');
            },

            selectOption(selectedIndex) {
                const q = appState.activeQuestions[appState.currentIndex];
                const optionsContainer = document.getElementById('options-container');
                const buttons = optionsContainer.getElementsByTagName('button');

                for (let i = 0; i < buttons.length; i++) {
                    buttons[i].disabled = true;
                    buttons[i].classList.add('cursor-default');
                    if (i === q.answer) {
                        buttons[i].classList.remove('border-slate-800', 'bg-slate-950/60');
                        buttons[i].classList.add('border-emerald-500/80', 'bg-emerald-500/10', 'text-emerald-300');
                    } else if (i === selectedIndex && selectedIndex !== q.answer) {
                        buttons[i].classList.remove('border-slate-800', 'bg-slate-950/60');
                        buttons[i].classList.add('border-rose-500/80', 'bg-rose-500/10', 'text-rose-300');
                    } else {
                        buttons[i].classList.add('opacity-50');
                    }
                }

                const isCorrect = (selectedIndex === q.answer);
                if (isCorrect) {
                    appState.score++;
                }

                const expBox = document.getElementById('explanation-box');
                const expTitle = document.getElementById('explanation-title');
                const expText = document.getElementById('explanation-text');

                expBox.classList.remove('hidden');
                if (isCorrect) {
                    expBox.className = "mt-6 p-5 rounded-xl border border-emerald-500/30 bg-emerald-950/20 space-y-3 animate-fade-in";
                    expTitle.innerHTML = `<i data-lucide="check-circle-2" class="w-5 h-5 text-emerald-400"></i><span class="text-emerald-400">ถูกต้อง! ยอดเยี่ยมมาก</span>`;
                } else {
                    expBox.className = "mt-6 p-5 rounded-xl border border-rose-500/30 bg-rose-950/20 space-y-3 animate-fade-in";
                    expTitle.innerHTML = `<i data-lucide="x-circle" class="w-5 h-5 text-rose-400"></i><span class="text-rose-400">ยังไม่ถูกต้อง ลองทบทวนวิธีคิดด้านล่างนี้</span>`;
                }
                expText.innerHTML = q.explanation;

                lucide.createIcons();

                const actionContainer = document.getElementById('action-container');
                actionContainer.classList.remove('hidden');
                
                const nextBtnText = document.getElementById('next-btn-text');
                if (appState.currentIndex === appState.activeQuestions.length - 1) {
                    nextBtnText.innerText = "ดูผลสรุปคะแนน";
                } else {
                    nextBtnText.innerText = "ข้อถัดไป";
                }

                document.getElementById('nav-score-badge').innerText = `คะแนนสะสม: ${appState.score}`;
            },

            nextQuestion() {
                appState.currentIndex++;
                if (appState.currentIndex < appState.activeQuestions.length) {
                    this.loadQuestion();
                } else {
                    this.showResults();
                }
            },

            showResults() {
                if (appState.timerInterval) clearInterval(appState.timerInterval);

                document.getElementById('screen-quiz').classList.add('hidden');
                document.getElementById('screen-result').classList.remove('hidden');

                const total = appState.activeQuestions.length;
                const percentage = (appState.score / total) * 100;

                document.getElementById('final-score').innerText = `${appState.score} / ${total}`;

                const totalTimeAllowed = appState.selectedTimerMinutes * 60;
                const elapsedSeconds = totalTimeAllowed - appState.timeLeft;
                const mins = String(Math.floor(elapsedSeconds / 60)).padStart(2, '0');
                const secs = String(elapsedSeconds % 60).padStart(2, '0');
                document.getElementById('final-time').innerText = `${mins}:${secs}`;

                const msgEl = document.getElementById('result-message');
                if (percentage >= 80) {
                    msgEl.innerText = "สุดยอด! คุณมีความพร้อมสูงมากสำหรับสนามสอบ A-Level Physics";
                } else if (percentage >= 50) {
                    msgEl.innerText = "ทำได้ดี! ทบทวนสูตรและจุดที่ผิดพลาดเพิ่มเติมอีกนิด จะทำคะแนนได้พุ่งกระฉูดแน่นอน";
                } else {
                    msgEl.innerText = "พยายามได้ดีครับ! ลองฝึกทำซ้ำอีกรอบเพื่อเสริมสร้างความเข้าใจในโจทย์คำนวณนะ";
                }
            },

            restartQuiz() {
                this.startQuiz(appState.currentCategory);
            },

            returnToHome() {
                if (appState.timerInterval) clearInterval(appState.timerInterval);
                document.getElementById('screen-quiz').classList.add('hidden');
                document.getElementById('screen-result').classList.add('hidden');
                document.getElementById('screen-home').classList.remove('hidden');
            },

            getCategoryName(cat) {
                const names = {
                    mechanics: 'กลศาสตร์',
                    electricity: 'ไฟฟ้าและแม่เหล็ก',
                    waves: 'คลื่นและแสง',
                    modern: 'ฟิสิกส์ยุคใหม่',
                    fluids: 'ของไหลและความตึงผิว',
                    thermo: 'ความร้อนและแก๊ส',
                    challenge: 'โหมดชาเลนจ์พิเศษ (⚡)',
                    all: 'รวมทุกหมวดหมู่'
                };
                return names[cat] || 'ฟิสิกส์ทั่วไป';
            }
        };

        window.onload = function() {
            lucide.createIcons();
        };
    </script>
</body>
</html>