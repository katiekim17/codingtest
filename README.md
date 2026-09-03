# codingtest

코딩테스트 풀이 모음.

## 구조

```
baekjoon/    # 백준
programmers/ # 프로그래머스
leetcode/    # 릿코드
```

파일명은 문제 번호로 (예: `baekjoon/1000.py`).

## 풀이 올리는 법

파일을 저장하는 것만으로는 GitHub에 올라가지 않는다.
문제를 풀 때마다 아래 3줄을 실행해야 잔디가 찍힌다.

```bash
cd ~/Documents/GitHub/codingtest
git add .
git commit -m "solve: 프로그래머스 12345"
git push
```

- `git add .` — 바뀐 파일 전부 담기
- `git commit -m "..."` — 담은 내용 기록 (메시지는 자유)
- `git push` — GitHub에 업로드 (이걸 해야 잔디 반영)

### 잔디가 안 찍힐 때

커밋 이메일이 GitHub 계정에 등록·verified 되어 있어야 한다.
확인: GitHub → Settings → Emails

```bash
git config user.email   # 현재 커밋에 쓰이는 이메일 확인
```
