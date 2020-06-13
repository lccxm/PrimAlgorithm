
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Prim {
    private static HashMap<Integer, List<Vertice>> verts;


    public static void main(String[] args) throws FileNotFoundException {
        load();
        PrimMST();
    }

    public static void load() throws FileNotFoundException {
        verts = new HashMap<>();
        File f = new File("tests/prim_10_sparse.dot");
        Scanner in = new Scanner(f);
        while (in.hasNextLine()) {
            String[] a = in.nextLine().split("\\D+");
            List<String> l1 = Arrays.asList(a);
            if (a.length >= 4) {
//                System.out.println(a[1]+", "+a[2]+", "+a[3]);
                Integer u = Integer.parseInt(a[1]);
                Integer v = Integer.parseInt(a[2]);
                Integer w = Integer.parseInt(a[3]);
                Vertice v1 = new Vertice(v);
                Vertice u1 = new Vertice(u);
                v1.w = w;
                u1.w = w;
//                System.out.println("v1: "+v1);
//                System.out.println("u1: "+u1);
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

//    public static void PrimMST() {
//       //List<Vertice> G = new LinkedList<>();
//        List<Vertice> visitados = new ArrayList<>();
//
//
//        PriorityQueue<Vertice> Q = new PriorityQueue<>();
//        for (Integer key : verts.keySet())
//            Q.add(new Vertice(key));
//        //System.out.println(Q);
//
//        List<Vertice> l = new LinkedList<>();
//        Vertice r = Q.peek();
//        r.chave = 0;
//        // System.out.println(Q);
//        int pesoArvoreMin = 0;
//        Vertice head = null;
//        while (!Q.isEmpty()) {
//            Vertice u = Q.poll();
//            //if(visitados.contains(u)) {
//                System.out.println("chave: "+u.chave);
//                pesoArvoreMin += u.chave;
//            //}
//            //System.out.println(Q);
//            //int menor = 9999;
//            //boolean flag = false;
//            List<Vertice> targets = verts.get(u.val);
//            for (Vertice v : targets){
//                if (w(u, v) < v.chave && Q.contains(v) /*& w(u, v)<menor*/) {
//                    visitados.add(v);
////                    System.out.println("----------");
////                    System.out.println("v" + v);
//                    Q.remove(v);
//                    //flag = true;
//                    //
//                    v.chave = w(u, v);
////                    System.out.println("u: " + u);
//                    v.prev = u;
//                    //System.out.println("------");
//                    //System.out.println(v);
//                    //menor = v.chave;
//                    //pesoArvoreMin += v.chave;
//                    Q.add(v);
//                    l.add(v);
////                    System.out.println("l: "+l);
////                    System.out.println("Q: "+Q);
//                    //System.out.print("added");
//                    //System.out.println(v);
//                    head = v;
//                }
//            }
//            //visitados.forEach(vertice -> System.out.println("chave: "+vertice.chave +"\nweight: "+vertice.w + "\nval: "+vertice.val + "\n------------"));
//            //if (flag)
//            //    pesoArvoreMin += menor;
///*             for (Vertice v : Q) {
//                if (w(u, v) != -1 && w(u, v) < v.chave) {
//                    v.chave = w(u, v);
//                    menor = v.chave;
//                    l.add(v);
//                    System.out.print("added");
//                    System.out.println(v);
//                }
//            } */
//            //System.out.println(menor);
//            //pesoArvoreMin += menor;
//        }
//        /*while (head!=null){
//            System.out.println(head);
//            head = head.prev;
//        }*/
//        // System.out.println(pesoArvoreMin);
//        //System.out.println(l);
//        System.out.print("Peso total: ");
//        System.out.println(pesoArvoreMin);
//        System.out.println("Esperado: 26");
//    }


    public static void PrimMST(){
        List<Vertice> visitados = new ArrayList<>();

        PriorityQueue<Vertice> Q = new PriorityQueue<>();
        for (Integer key : verts.keySet()) {
            Q.add(new Vertice(key));
        }
        //System.out.println(Q);
        Vertice r = Q.peek();
        Q.remove(r);
        r.chave = 0;
        Q.add(r);
        while(!Q.isEmpty()){
            Vertice v = Q.poll();
            //System.out.println("v: "+v);
            visitados.add(v);
            List<Vertice> targets = verts.get(v.val);
            for (Vertice a : targets){
                if(!visitados.contains(a) && !a.visitado) {
                    System.out.println("a: "+a);
//                    System.out.println("chave: " + a.chave);
//                    System.out.println("peso: " + w(v, a));
                    if (a.chave > w(v, a) && Q.contains(a)) {
                        Q.remove(a);
                        a.chave = w(v, a);
                        a.prev = v;
                        a.visitado = true;
                        Q.add(a);
                    }
                }
            }
        }
        int total = 0;
        for(Vertice v: visitados){
            System.out.println(v.chave);
            total += v.chave;
        }
        //total -= 9999;
        System.out.println("total: "+total);
//        System.out.println(visitados);

//        9999
//        2
//        9
//        1
//        4
//        1
//        11
//        6
//        6

    }
}