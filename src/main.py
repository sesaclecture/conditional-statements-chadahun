"""
Implement User Management System
"""
from login_sys import Loginsystem




if __name__ == '__main__':
    loginsys = Loginsystem()
    while True:
        print("====== 사용자 관리 시스템 ======")
        print("1. 회원가입 (Register)")
        print("2. 로그인 (Login)")
        print("3. 정보 수정 (Edit User)")
        print("4. 계정 삭제 (Delete User)")
        print("any key. 종료 (Exit)")
        choice = input("선택하세요: ")

        if choice == '1':
            print("\n[회원가입]")
            name = input("이름: ")
            birthday = input("생년월일 (YYYYMMDD): ")
            user_id = input("ID: ")
            password = input("비밀번호: ")
            role = input("역할 (viewer/editor/admin): ")

            loginsys.register_user(name, birthday, user_id, password, role)

        elif choice == '2':
            print("\n[로그인]")
            user_id = input("ID: ")
            password = input("비밀번호: ")

            loginsys.login(user_id, password)

        elif choice == '3':
            print("\n[정보 수정]")
            target_id = input("수정할 사용자 ID: ")
            new_name = input("새 이름 (Enter 생략 가능): ")
            new_password = input("새 비밀번호 (Enter 생략 가능): ")

            new_name = new_name if new_name else None
            new_password = new_password if new_password else None

            loginsys.edit_user(target_id, new_name, new_password)

        elif choice == '4':
            print("\n[계정 삭제]")
            target_id = input("삭제할 사용자 ID: ")
            loginsys.delete_user(target_id)

        else:
            print("프로그램을 종료합니다.")
            break