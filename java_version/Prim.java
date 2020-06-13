
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Prim {
    private static HashMap<Integer, List<Vertice>> verts;


    public static void main(String[] args) throws FileNotFoundException {
        load();
        PrimMST();
    }

    public static void load() throws FileNotFoundException {
        verts = new HashMap<>();
        File f = new File("tests/prim_50_sparse.dot");
        Scanner in = new Scanner(f);
        while (in.hasNextLine()) {
            String[] a = in.nextLine().split("\\D+");
            List<String> l1 = Arrays.asList(a);
            if (a.length >= 4) {
                System.out.println(a[1]+", "+a[2]+", "+a[3]);
                Integer u = Integer.parseInt(a[1]);
                Integer v = Integer.parseInt(a[2]);
                Integer w = Integer.parseInt(a[3]);
                Vertice v1 = new Vertice(v);
                Vertice u1 = new Vertice(u);
                v1.w = w;
                u1.w = w;
                if (!verts.containsKey(u)) {
                    List<Vertice> l = new LinkedList<>();
                    l.add(v1);
                    verts.put(u, l);
                } else {
                    verts.get(u).add(v1);
                }
                //
                if (!verts.containsKey(v)) {
                    List<Vertice> l = new LinkedList<>();
                    l.add(u1);
                    verts.put(v, l);
                } else {
                    verts.get(v).add(u1);
                }
            }
        }
        in.close();
        //System.out.println(verts);
    }

    public static int w(Vertice u, Vertice v) {
        List<Vertice> adj = verts.get(u.val);
        for (Vertice vert: adj)
            if (vert.val == v.val)
                return vert.w;
        return -1;}
        /* for (int i = 0; i < mat.length; i++) {
            if (mat[i][0] == x && mat[i][1] == y)
                return mat[i][2];
            if (mat[i][1] == x && mat[i][0] == y)
                return mat[i][2];
        }
        return -1; */

    public static void PrimMST() {
       //List<Vertice> G = new LinkedList<>();
        PriorityQueue<Vertice> Q = new PriorityQueue<>();
        for (Integer key : verts.keySet())
            Q.add(new Vertice(key));
        //System.out.println(Q);

        List<Vertice> l = new LinkedList<>();
        Vertice r = Q.peek();
        r.chave = 0;
        // System.out.println(Q);
        int pesoArvoreMin = 0;
        Vertice head = null;
        while (!Q.isEmpty()) {
            Vertice u = Q.poll();
            pesoArvoreMin += u.chave;
            //System.out.println(Q);
            //int menor = 9999;
            //boolean flag = false;
            List<Vertice> targets = verts.get(u.val);
            for (Vertice v : targets){
                if (w(u, v) < v.chave && Q.contains(v)/*& w(u, v)<menor*/) {
                    Q.remove(v);
                    //flag = true;
                    //
                    v.chave = w(u, v);
                    v.prev = u;
                    //menor = v.chave;
                    //pesoArvoreMin += v.chave;
                    Q.add(v);
                    l.add(v);
                    //System.out.print("added");
                    //System.out.println(v);
                    head = v;
                }
            }
            //if (flag)
            //    pesoArvoreMin += menor;
/*             for (Vertice v : Q) {
                if (w(u, v) != -1 && w(u, v) < v.chave) {
                    v.chave = w(u, v);
                    menor = v.chave;
                    l.add(v);
                    System.out.print("added");
                    System.out.println(v);
                }
            } */
            //System.out.println(menor);
            //pesoArvoreMin += menor;
        }
        /*while (head!=null){
            System.out.println(head);
            head = head.prev;
        }*/
        // System.out.println(pesoArvoreMin);
        //System.out.println(l);
        System.out.print("Peso total: ");
        System.out.println(pesoArvoreMin);
        System.out.println("Esperado: 10"); 
    }
}