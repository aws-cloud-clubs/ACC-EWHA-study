#include<vector>
#include<queue>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int n = maps.size(); // 맵의 크기 
    int m = maps[0].size(); // 인덱스 하나의 크기 
    
    int answer = 0;
    
    int dx[4] = {-1,1,0,0};
    int dy[4] = {0,0,-1,1};
    
    queue<pair<int, int>> q; // (x,y) 페어를 저장할 큐 선언 
    q.push({0,0});
    
    while(!q.empty()){
        int x = q.front().first; // 행 번호 
        int y = q.front().second; // 열 번호 
        q.pop(); // 처음 꺼낸 좌표는 큐에서 제거 
        
        
        for(int i=0; i<4; i++){ 
            int nx = x+dx[i]; // 행 이동 
            int ny = y+dy[i]; // 열 이동 
            
            if (nx< 0 || ny <0 || nx >= n || ny >=m ) continue; 
            if(maps[nx][ny] !=1) continue; 
            
            maps[nx][ny] = maps[x][y] + 1; // 한 칸 이동 
            q.push({nx, ny}); 
            
            
        }
    }
    if (maps[n-1][m-1] == 1)
        answer = -1;
    else 
        answer = maps[n-1][m-1]; // 최단 거리값이 저장된 인덱스 
    
    

    return answer;
}