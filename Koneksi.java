
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author 672021039
 */
public class Koneksi {

    private static Connection koneksi;

    public static Connection getConnection() throws SQLException {
        String db = "jdbc:mysql://localhost:3306/database_crud";
        String user = "root";
        String pass = "";

        if (koneksi == null) {
            koneksi = (Connection) DriverManager.getConnection(db, user, pass);
        }
        return koneksi;
    }
}
