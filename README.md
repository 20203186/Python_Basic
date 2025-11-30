# 오픈소스 SW개론 03분반 과제 2

20203186 컴퓨터공학과 조성진

---

### <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/aa4ebe4f-4bf9-43cf-92ee-988ff7acc5d6" /> 개요

위 문서는 **리눅스** 명령어 중에서 top, ps, jobs, kill에 대해서 조사한 내용을 정리하고 있습니다.

---

### 1. 🔝 'top' 명령어


'top' 명령어는 현 운영체제의 **실시간 상태를** 모니터링하는 데 사용됩니다. 특히 CPU, 메모리 사용률, 현재 실행중인 프로세스 목록 및 활동을 동적으로 보여줍니다.

| 항목 | 설명 |
| :---| :--- |
| **기능** | 시스템 resource 사용 현황, 및 프로세스 목록의 실시간 표시|
| **주요 정보** | PID, USER, PR&NI, VIRT, RES, %CPU, %MEM, 등 |
| **주요 KEY** | *k: kill*, *r: nice 값 변경*, *P: CPU 사용률 기준 정렬*, *M: 메모리 사용 기준 정렬*, *q: 종료* |

> 'top'은 시스템 부하를 빠르게 파악하는 데 유용하며, 작업관리자과 유사합니다.

---

### 2. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/7296a32f-0778-4fdf-9d70-242720c7e880" /> 'ps' 명령어

'ps(Process Status)' 명령어는 현재 시스템에서 **실행중인 프로세스들의** 스냅샷을 보여주며 'top'과는 달리 정적인 정보입니다.

| 옵션 | 설명 |
| ps -ef| 가장 많이 사용하는 명령어, 실행중인 모든 프로세스를 풀 포맷으로 출력 |
| ps aux | BSD 문법으로 모든 프로세스를 출력하고 싶을 때 사용, -ef와 차이점은 출력 형식이 다르다는 점|
| ps -l | Long format 으로 출력|

> 특정 사용자나 이름을 가진 프로세스를 찾을 때 'ps aux | grep [건색어]' 형태로 파이프와 그랩을 함께 사용 가능합니다.

---

### 3. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/13e54071-17ba-45ae-9487-fa6a2a64af67" /> 'jobs' 명령어

'jobs' 명령어는 현재 세션에서 백그라운드, 정지 상태로 실행되고 있는 **작업 목록**을 보여줍니다.

| 옵션 | 설명 |
| -L | 각 작업의 프로세스 ID(PID)를 함께 출력 |
| -p | 각 작업의 프로세스 ID만 출력 |
| -n | 가장 최근에 상태가 변경된 작업만 출력 |
| -r | Running인 작업만 출력 |

>  jobs 명령어를 통해 각 작업의 작업번호를 확인하고, 다른 명령어를 사용해 작업을 foreground로 전환하거나 background로 전환, 또는 종료가 가능합니다. 다수의 작업을 동시에 처리 시 효과적으로 관리할 수 있도록 도와줍니다.

---

### 4. <img width="16" height="16" alt="image" src="https://github.com/user-attachments/assets/c08b84e3-df10-4764-b38e-36078686dead" /> 'kill' 명령어

'kill' 명령어는 지정된 PID 를 가진 프로세스에게 신호를 보내 **프로세스를 제어**하는 데 사용됩니다. 일반적으로 프로세스를 종료하는 데 사용됩니다.

| 주요 시그널(번호) | 설명 |
| SIGHUP(1) | bash 쉘을 reload 하거나 restart하도록 유도하는 데 사용됩니다. 설정 파일을 다시 읽어오는 등의 역할을 수행합니다.|
| SIGINT(2) | Ctrl+C와 같은 역할, 정상 종료를 요청합니다. |
| SIGKILL(9) | python3 프로세스를 즉시 강제종료 하는 시그널입니다. 프로세스가 응답하지 않을 시 유용하며, 해당 프로세스는 강제로 메모리에서 제거됩니다. |
| SIGTERM(15) | 이 명령어는 특텅 PID를 가진 python3 프로세스에게 시그널을 보내 정상 종료를 요청합니다. 프로세스가 정상 종료하도록 유도하지만 이를 무시하거나 응답하지 않을 수 있습니다. |

> **사용법** 'kill [옵션/시그널(-1, -2, -9)] [PID]'
> 'kill [PID]' -> Default signal 15 (정상 종료)

---
