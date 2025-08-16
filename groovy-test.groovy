import groovy.json.JsonSlurper
// import com.eviware.soapui.support.GroovyUtils

def projectDir = new GroovyUtils(context).projectPath

File procsEntrada = new File(projectDir + "/input.txt")

if(!procsEntrada.exists()) {
    log.error "Input file not found at: " + procsEntrada.absolutePath
    testRunner.fail("Input file not found.")
    return
}

def List listaProcessos = procsEntrada.readLines()