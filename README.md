# 오픈소스 SW개론 03분반 과제 2

20203186 컴퓨터공학과 조성진

---

### <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/aa4ebe4f-4bf9-43cf-92ee-988ff7acc5d6" /> 개요

위 문서는 **리눅스** 명령어 중에서 top, ps, jobs, kill에 대해서 조사한 내용을 정리하고 있습니다.

---

### 1. 🔝 명령어


'top' 명령어는 시스템의 **실시간 상태를** 모니터링하는 데 사용됩니다. 특히 CPU, 메모리 사용률, 현재 실행중인 프로세스 목록 및 활동을 동적으로 보여줍니다.

| 항목 | 설명 |
| :---| :--- |
| **기능** | 시스템 resource 사용 현황, 및 프로세스 목록의 실시간 표시|
| **주요 정보** | PID, USER, PR, NI, VIRT, RES, %CPU, %MEM, 등 |
| **주요 KEY** | *k: kill*, *r: nice 값 변경*, *P: CPU 사용률 기준 정렬*, *M: 메모리 사용 기준 정렬*, *q: 종료* |
