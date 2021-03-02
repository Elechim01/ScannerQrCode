//
//  ContentView.swift
//  ScannerQrCode
//
//  Created by Michele Manniello on 02/03/21.
//

import SwiftUI
import CodeScanner

struct ContentView: View {
    @State var isShowingScanner = false
    var body: some View {
        Button(action: {
            self.isShowingScanner = true
        }, label: {
            Text("Mostra Scanner")
        })
        .sheet(isPresented: $isShowingScanner, content: {
            CodeScannerView(codeTypes: [.qr], simulatedData: "Some simulated data",completion: self.handleScan)
            })
    }
    private func handleScan(result: Result<String, CodeScannerView.ScanError>) {
           self.isShowingScanner = false
        switch result{
        case .success(let data):
            print("Sucess with \(data)")
            UIApplication.shared.open(URL(string: data)!)
            
        case .failure(let error):
            print("Sucess with \(error)")
        }
    }
   
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
