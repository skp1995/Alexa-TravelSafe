package com.example.harshailluri.safedrive;

import android.location.Location;
import android.os.Bundle;

import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;

import static android.provider.ContactsContract.CommonDataKinds.Website.URL;

public class locationClass implements android.location.LocationListener {
    private static double lat, lon;

    @Override
    public void onLocationChanged(Location location) {
        System.out.println("hello");
        System.out.println(location.getLongitude());
        System.out.println(location.getLatitude());
        lat = location.getLatitude();
        lon = location.getLongitude();



    }
    public static double getLat(){
        return lat;
    }
    public static double getLon(){
        return lon;
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {

    }

    @Override
    public void onProviderEnabled(String provider) {

    }

    @Override
    public void onProviderDisabled(String provider) {

    }
}
