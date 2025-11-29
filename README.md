# 오픈소스 SW개론 03분반 과제 2

20203186 컴퓨터공학과 조성진

---

### <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/aa4ebe4f-4bf9-43cf-92ee-988ff7acc5d6" /> 개요

위 문서는 **리눅스** 명령어 중에서 top, ps, jobs, kill에 대해서 조사한 내용을 정리하고 있습니다.

---

### 1. 🔝 'top' 명령어


'top' 명령어는 시스템의 **실시간 상태를** 모니터링하는 데 사용됩니다. 특히 CPU, 메모리 사용률, 현재 실행중인 프로세스 목록 및 활동을 동적으로 보여줍니다.

| 항목 | 설명 |
| :---| :--- |
| **기능** | 시스템 resource 사용 현황, 및 프로세스 목록의 실시간 표시|
| **주요 정보** | PID, USER, PR, NI, VIRT, RES, %CPU, %MEM, 등 |
| **주요 KEY** | *k: kill*, *r: nice 값 변경*, *P: CPU 사용률 기준 정렬*, *M: 메모리 사용 기준 정렬*, *q: 종료* |

> 'top'은 시스템 부하를 빠르게 파악하는 데 유용하며, 작업관리자과 유사합니다.

---

### 2. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/7296a32f-0778-4fdf-9d70-242720c7e880" /> 'ps' 명령어

'ps' 명령어는 현재 시스템에서 실행중인 프로세스들의 스냅샷을 보여주며 'top'과는 달리 정적인 정보입니다.

| 옵션 | 설명 |
| ps aux | |

> 특정 사용자나 이름을 가진 프로세스를 찾을 때 'ps aux | grep [건색어]' 형태로 파이프와 그랩을 함께 사용합니다.

---

### 3. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/13e54071-17ba-45ae-9487-fa6a2a64af67" /> 'jobs' 명령어

'jobs' 명령어는 현재 쉘에서 백그라운드, 정지 상태로 실행되고 있는 작업 목록을 보여줍니다.

| | |

>  ㅇㅇ

---

### 4. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/c08b84e3-df10-4764-b38e-36078686dead" /> 'kill' 명령어

'kill' 명령어는 지정된 PID 를 가진 프로세스에게 신호를 보내 프로세스를 제어하는 데 사용됩니다. 일반적으로 프로세스를 종료하는 데 사용됩니다.

