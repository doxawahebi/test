import gdb

class FetchBp(gdb.Breakpoint):
    def stop(self):
        # x86_64 레지스터 $esi를 읽어와 객체 번호로 출력
        num = gdb.parse_and_eval("$esi")
        print(f"Fetching Object Num: {num}")
        
        # False를 리턴하면 프롬프트를 띄우지 않고 자동으로 continue 됨
        return False

# XRef::fetch 함수에 중단점 걸기
FetchBp("XRef::fetch")