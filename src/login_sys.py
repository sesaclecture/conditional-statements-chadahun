from datetime import datetime

class Loginsystem:
    def __init__(self):
        self.user_info = {
            1: {
                'name': 'elice',
                'birthday': '20080526',
                'id': 'eli',
                'password': 'qwe123@!',
                'role': 'viewer'
            },
            2: {
                'name': 'Tom',
                'birthday': '19990526',
                'id': 'tom',
                'password': '123456@!',
                'role': 'editor'
            },
            3: {
                'name': 'jake',
                'birthday': '19500526',
                'id': 'jak',
                'password': 'wqe!35@!',
                'role': 'admin'
            }
        }
        self.logged_in_user = None
        self.print_all_users()

    def is_valid_birth(self, birth: str):
        try:
            datetime.strptime(birth, '%Y%m%d')
            return True
        except ValueError:
            return False

    def is_valid_id(self, new_id: str):
        return all(user['id'] != new_id for user in self.user_info.values())

    def is_secure_password(self, pwd: str):
        return len(pwd) >= 10 and any(not c.isalnum() for c in pwd)

    def print_all_users(self):
        print("\n[전체 사용자 목록]")
        for uid, info in self.user_info.items():
            print(f"[UID {uid}] {info}")
        print()

    def get_uid_by_id(self, user_id):
        for uid, info in self.user_info.items():
            if info['id'] == user_id:
                return uid
        return None

    def register_user(self, name, birthday, user_id, password, role):
        if not self.is_valid_birth(birthday):
            print("유효하지 않은 생년월일입니다.")
            return

        if not self.is_valid_id(user_id):
            print("중복된 ID입니다.")
            return

        if not self.is_secure_password(password):
            print("비밀번호는 10자 이상, 특수문자 포함이어야 합니다.")
            return

        new_uid = max(self.user_info.keys()) + 1
        self.user_info[new_uid] = {
            'name': name,
            'birthday': birthday,
            'id': user_id,
            'password': password,
            'role': role
        }

        print(f"사용자 '{user_id}' 등록 완료 (UID {new_uid})")
        self.print_all_users()

    def login(self, user_id, password):
        for uid, info in self.user_info.items():
            if info['id'] == user_id and info['password'] == password:
                self.logged_in_user = (uid, info)
                print(f"로그인 성공! (역할: {info['role']})")
                return
        print("로그인 실패: 아이디 또는 비밀번호가 틀립니다.")

    def edit_user(self, target_id, new_name=None, new_password=None):
        if self.logged_in_user is None:
            print("먼저 로그인하세요.")
            return

        my_uid, my_info = self.logged_in_user
        my_role = my_info['role']
        target_uid = self.get_uid_by_id(target_id)

        if target_uid is None:
            print("대상 ID가 존재하지 않습니다.")
            return

        if my_role == 'viewer' and my_uid != target_uid:
            print("viewer는 자신의 정보만 수정할 수 있습니다.")
            return

        if new_name:
            self.user_info[target_uid]['name'] = new_name
        if new_password:
            if self.is_secure_password(new_password):
                self.user_info[target_uid]['password'] = new_password
            else:
                print("비밀번호 조건을 만족하지 않습니다.")
                return

        print(f"사용자 '{target_id}' 정보 수정 완료.")
        self.print_all_users()

    def delete_user(self, target_id):
        if self.logged_in_user is None:
            print("먼저 로그인하세요.")
            return

        my_uid, my_info = self.logged_in_user
        my_role = my_info['role']
        target_uid = self.get_uid_by_id(target_id)

        if target_uid is None:
            print("대상 ID가 존재하지 않습니다.")
            return

        if my_role in ['viewer', 'editor'] and my_uid != target_uid:
            print("viewer/editor는 자신의 계정만 삭제할 수 있습니다.")
            return

        del self.user_info[target_uid]
        print(f"사용자 '{target_id}' 삭제 완료.")
        self.print_all_users()
