//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2019.02.08 at 04:20:20 PM KST 
//


package com.microsoft.Malmo.Schemas;

import javax.xml.bind.annotation.XmlEnum;
import javax.xml.bind.annotation.XmlEnumValue;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for HumanLevelCommand.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * <p>
 * <pre>
 * &lt;simpleType name="HumanLevelCommand">
 *   &lt;restriction base="{http://www.w3.org/2001/XMLSchema}string">
 *     &lt;enumeration value="forward"/>
 *     &lt;enumeration value="left"/>
 *     &lt;enumeration value="back"/>
 *     &lt;enumeration value="right"/>
 *     &lt;enumeration value="jump"/>
 *     &lt;enumeration value="sneak"/>
 *     &lt;enumeration value="sprint"/>
 *     &lt;enumeration value="inventory"/>
 *     &lt;enumeration value="swapHands"/>
 *     &lt;enumeration value="drop"/>
 *     &lt;enumeration value="use"/>
 *     &lt;enumeration value="attack"/>
 *     &lt;enumeration value="pickItem"/>
 *     &lt;enumeration value="hotbar.1"/>
 *     &lt;enumeration value="hotbar.2"/>
 *     &lt;enumeration value="hotbar.3"/>
 *     &lt;enumeration value="hotbar.4"/>
 *     &lt;enumeration value="hotbar.5"/>
 *     &lt;enumeration value="hotbar.6"/>
 *     &lt;enumeration value="hotbar.7"/>
 *     &lt;enumeration value="hotbar.8"/>
 *     &lt;enumeration value="hotbar.9"/>
 *     &lt;enumeration value="moveMouse"/>
 *   &lt;/restriction>
 * &lt;/simpleType>
 * </pre>
 * 
 */
@XmlType(name = "HumanLevelCommand")
@XmlEnum
public enum HumanLevelCommand {

    @XmlEnumValue("forward")
    FORWARD("forward"),
    @XmlEnumValue("left")
    LEFT("left"),
    @XmlEnumValue("back")
    BACK("back"),
    @XmlEnumValue("right")
    RIGHT("right"),
    @XmlEnumValue("jump")
    JUMP("jump"),
    @XmlEnumValue("sneak")
    SNEAK("sneak"),
    @XmlEnumValue("sprint")
    SPRINT("sprint"),
    @XmlEnumValue("inventory")
    INVENTORY("inventory"),
    @XmlEnumValue("swapHands")
    SWAP_HANDS("swapHands"),
    @XmlEnumValue("drop")
    DROP("drop"),
    @XmlEnumValue("use")
    USE("use"),
    @XmlEnumValue("attack")
    ATTACK("attack"),
    @XmlEnumValue("pickItem")
    PICK_ITEM("pickItem"),
    @XmlEnumValue("hotbar.1")
    HOTBAR_1("hotbar.1"),
    @XmlEnumValue("hotbar.2")
    HOTBAR_2("hotbar.2"),
    @XmlEnumValue("hotbar.3")
    HOTBAR_3("hotbar.3"),
    @XmlEnumValue("hotbar.4")
    HOTBAR_4("hotbar.4"),
    @XmlEnumValue("hotbar.5")
    HOTBAR_5("hotbar.5"),
    @XmlEnumValue("hotbar.6")
    HOTBAR_6("hotbar.6"),
    @XmlEnumValue("hotbar.7")
    HOTBAR_7("hotbar.7"),
    @XmlEnumValue("hotbar.8")
    HOTBAR_8("hotbar.8"),
    @XmlEnumValue("hotbar.9")
    HOTBAR_9("hotbar.9"),
    @XmlEnumValue("moveMouse")
    MOVE_MOUSE("moveMouse");
    private final String value;

    HumanLevelCommand(String v) {
        value = v;
    }

    public String value() {
        return value;
    }

    public static HumanLevelCommand fromValue(String v) {
        for (HumanLevelCommand c: HumanLevelCommand.values()) {
            if (c.value.equals(v)) {
                return c;
            }
        }
        throw new IllegalArgumentException(v);
    }

}
