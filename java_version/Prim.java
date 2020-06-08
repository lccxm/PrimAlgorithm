
 import java.util.LinkedList;
 import java.util.List;
 import java.util.PriorityQueue;
 import java.util.Queue;

 public class Prim{
    public static int[][] mat;
    public static void main(String[] args) {
        mat = new int[][]{
                {0, 2, 11},
                {1, 2, 18},
                {1, 3, 1},
                {2, 7, 11},
                {3, 5, 14},
                {4, 6, 12},
                {5, 6, 8},
                {7, 8, 14},
                {7, 9, 5}
        }; //esperado: 94

        /*
        for (int i=0;i<mat.length;i++)
            for (int j=0;j<mat[i].length;j++)
                System.out.println(mat[i][j]);
        */
        Prim();
    }
    public static int w(int x, int y){
        for (int i=0;i<mat.length;i++) {
            if (mat[i][0] == x && mat[i][1] == y)
                return mat[i][2];
            if (mat[i][1] == x && mat[i][0] == y)
                return mat[i][2];
        }
        return -1;
    }

    public static void Prim(){
        //List<Vertice> G = new LinkedList<>();
        PriorityQueue<Vertice> Q = new PriorityQueue<>();
        for (int i=0;i<mat.length;i++) {
            if (!Q.contains(new Vertice(mat[i][0])))
                Q.add(new Vertice(mat[i][0]));
            if (!Q.contains(new Vertice(mat[i][1])))
                Q.add(new Vertice(mat[i][1]));
        }
        List<Vertice> l = new LinkedList<>();
        Vertice r = Q.peek();
        r.chave = 0;
        //System.out.println(Q);
        int pesoArvoreMin = 0;
        while (!Q.isEmpty()){
            Vertice u = Q.poll();
            //System.out.println(u);
            //int menor = 9999;
            for (Vertice v : Q){
                if (w(u.val, v.val) !=-1 && w(u.val, v.val) < v.chave) {
                    v.chave = w(u.val, v.val);
                    //menor = w(u.val, v.val);
                    l.add(v);
                }
            }
            //pesoArvoreMin += menor;
        }
        int res = 0;
        for (Vertice v : l)
            res +=v.chave;
        //System.out.println(pesoArvoreMin);
        System.out.println(l);
        System.out.print("Peso total: ");
        System.out.println(res);
        System.out.println("Esperado: 94");
    }
}