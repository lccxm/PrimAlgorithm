// Grupo: Gustavo Demicheie  Lucca Molon
// Implementa o algoritmo de Prim utilizando uma fila de prioridade.

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class P2 {
    private static HashMap<Integer, List<Vertice>> verts;
    private static String fileName;

    public static void main(String[] args) throws FileNotFoundException {
        fileName = args[0];
        load();
        PrimMST();
    }

    public static void load() throws FileNotFoundException {
        verts = new HashMap<>();
        File f = new File(fileName);
        Scanner in = new Scanner(f);
        while (in.hasNextLine()) {
            String[] a = in.nextLine().split("\\D+");
            if (a.length >= 4) {
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
    }

    public static int w(Vertice u, Vertice v) {
        List<Vertice> adj = verts.get(u.val);
        for (Vertice vert: adj)
            if (vert.val == v.val)
                return vert.w;
        return -1;}

    public static Vertice extractMin(List<Vertice> vertices){
        Integer menor =9999;
        Vertice vertice = null;
        for (Vertice v: vertices){
            if (v.chave<=menor){
                vertice = v;
                menor = v.chave;
            }
        }
        vertices.remove(vertice);
        return vertice;
    }

    public static void PrimMST(){
        List<Vertice> visitados = new ArrayList<>();
        PriorityQueue<Vertice> Q = new PriorityQueue<>();
        for (Integer key : verts.keySet()) {
            Q.add(new Vertice(key));
        }
        Vertice r = Q.poll();
        r.chave = 0;
        Q.add(r);
        visitados.add(r);
        while(!Q.isEmpty()){
            Vertice v = Q.poll();
            visitados.add(v);
            List<Vertice> targets = verts.get(v.val);
            for (Vertice a : targets){
                if(!visitados.contains(a) && !a.visitado) {
                    if (a.chave > w(v, a) && Q.contains(a)) {
                        a.chave = w(v, a);
                        a.prev = v;
                        a.visitado = true;
                    }
                }
            }
            List<Vertice> l1 = new ArrayList<>(Q);
            for(Vertice t : targets){
                for(Vertice l : l1){
                    if(t.val == l.val && t.chave < l.chave){
                        Q.remove(l);
                        Q.add(t);
                    }
                }
            }
        }

        int total = 0;
        for(Vertice u: visitados){
            total += u.chave;
        }
        System.out.println(total);
    }
}