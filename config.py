## Hidding superior menu and edditing footer
css_changes = """
<style>
#MainMenu {
    visibility:visible;
    }
footer{
    visibility:visible;
    }
footer:after{
    content: " using GISAID data. We are grateful to the data contributors who shared the data used in this Web Application via the GISAID Initiative: the Authors, the Originating Laboratories responsible for obtaining the specimens, and the Submitting Laboratories that generated the genetic sequences and metadata. All data in GISAID are subject to GISAID’s Terms and Conditions.   Elbe, S., and Buckland-Merrett, G. (2017) Data, disease and diplomacy: GISAID’s innovative contribution to global health. Global Challenges , 1:33-46. DOI: 10.1002/gch2.1018 PMCID: 31565258"
</style>
"""